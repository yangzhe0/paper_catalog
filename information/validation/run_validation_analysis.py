#!/usr/bin/env python3
"""Generate validation tables/figures/docs from absolute_03_correction.csv."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DEFAULT_INPUT = Path("/data/sues01/Ancoj/result/absolute_03_correction.csv")
DEFAULT_REPORT = Path("/data/sues01/Ancoj/result/absolute_03_report.csv")
DEFAULT_OUTPUT_ROOT = Path("/data/sues01/Ancoj/validation/results")


@dataclass
class Scenario:
    name: str
    desc: str
    mask: pd.Series
    illustrative_only: bool = False


def normalize_text_col(s: pd.Series, empty_value: str = "unknown") -> pd.Series:
    out = s.fillna(empty_value).astype(str).str.strip().str.lower()
    return out.replace("", empty_value)


def safe_pct(before, after):
    b = np.asarray(before, dtype=float)
    a = np.asarray(after, dtype=float)
    out = np.full(np.shape(b), np.nan, dtype=float)
    valid = np.isfinite(b) & np.isfinite(a) & (b != 0)
    out[valid] = (b[valid] - a[valid]) / b[valid] * 100.0
    if out.shape == ():
        return float(out)
    return out


def metric_block(g: pd.DataFrame) -> Dict[str, float]:
    b_ra = np.abs(g["dRAcosDec_before_arcsec"].to_numpy(dtype=float))
    a_ra = np.abs(g["dRAcosDec_after_arcsec"].to_numpy(dtype=float))
    b_de = np.abs(g["dDec_before_arcsec"].to_numpy(dtype=float))
    a_de = np.abs(g["dDec_after_arcsec"].to_numpy(dtype=float))
    b_n = np.hypot(g["dRAcosDec_before_arcsec"].to_numpy(dtype=float), g["dDec_before_arcsec"].to_numpy(dtype=float))
    a_n = np.hypot(g["dRAcosDec_after_arcsec"].to_numpy(dtype=float), g["dDec_after_arcsec"].to_numpy(dtype=float))

    ra_imp = a_ra < b_ra
    de_imp = a_de < b_de
    n_imp = a_n < b_n

    return {
        "N": int(len(g)),
        "improve_rate_norm": float(np.mean(n_imp)),
        "improve_rate_ra": float(np.mean(ra_imp)),
        "improve_rate_dec": float(np.mean(de_imp)),
        "improve_rate_both": float(np.mean(ra_imp & de_imp)),
        "worse_rate_both": float(np.mean((~ra_imp) & (~de_imp))),
        "tradeoff_rate_one_improve_one_worse": float(np.mean((ra_imp & (~de_imp)) | ((~ra_imp) & de_imp))),
        "med_norm_before_arcsec": float(np.median(b_n)),
        "med_norm_after_arcsec": float(np.median(a_n)),
        "med_norm_improve_pct": float(safe_pct(np.median(b_n), np.median(a_n))),
        "p95_norm_before_arcsec": float(np.percentile(b_n, 95)),
        "p95_norm_after_arcsec": float(np.percentile(a_n, 95)),
        "p95_norm_improve_pct": float(safe_pct(np.percentile(b_n, 95), np.percentile(a_n, 95))),
        "mean_norm_before_arcsec": float(np.mean(b_n)),
        "mean_norm_after_arcsec": float(np.mean(a_n)),
        "mean_norm_improve_pct": float(safe_pct(np.mean(b_n), np.mean(a_n))),
        "rms_norm_before_arcsec": float(np.sqrt(np.mean(b_n * b_n))),
        "rms_norm_after_arcsec": float(np.sqrt(np.mean(a_n * a_n))),
        "rms_norm_improve_pct": float(safe_pct(np.sqrt(np.mean(b_n * b_n)), np.sqrt(np.mean(a_n * a_n)))),
        "med_abs_ra_before_arcsec": float(np.median(b_ra)),
        "med_abs_ra_after_arcsec": float(np.median(a_ra)),
        "med_abs_ra_improve_pct": float(safe_pct(np.median(b_ra), np.median(a_ra))),
        "med_abs_dec_before_arcsec": float(np.median(b_de)),
        "med_abs_dec_after_arcsec": float(np.median(a_de)),
        "med_abs_dec_improve_pct": float(safe_pct(np.median(b_de), np.median(a_de))),
    }


def plot_cdf(g: pd.DataFrame, title: str, out_png: Path) -> None:
    b_n = np.hypot(g["dRAcosDec_before_arcsec"].to_numpy(dtype=float), g["dDec_before_arcsec"].to_numpy(dtype=float))
    a_n = np.hypot(g["dRAcosDec_after_arcsec"].to_numpy(dtype=float), g["dDec_after_arcsec"].to_numpy(dtype=float))

    def cdf_xy(x: np.ndarray):
        xs = np.sort(x)
        ys = (np.arange(len(xs)) + 1) / len(xs)
        return xs, ys

    xb, yb = cdf_xy(b_n)
    xa, ya = cdf_xy(a_n)

    plt.figure(figsize=(8, 5))
    plt.plot(xb, yb, label="Before", linewidth=2)
    plt.plot(xa, ya, label="After", linewidth=2)
    plt.xscale("log")
    plt.xlabel("rho residual norm [arcsec]")
    plt.ylabel("CDF")
    plt.title(title)
    plt.grid(alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png, dpi=180)
    plt.close()


def plot_delta_hist(g: pd.DataFrame, title: str, out_png: Path) -> None:
    b_n = np.hypot(g["dRAcosDec_before_arcsec"].to_numpy(dtype=float), g["dDec_before_arcsec"].to_numpy(dtype=float))
    a_n = np.hypot(g["dRAcosDec_after_arcsec"].to_numpy(dtype=float), g["dDec_after_arcsec"].to_numpy(dtype=float))
    d = a_n - b_n

    q01, q99 = np.percentile(d, [1, 99])
    d = d[(d >= q01) & (d <= q99)]

    plt.figure(figsize=(8, 5))
    plt.hist(d, bins=80, alpha=0.85)
    plt.axvline(0.0, linestyle="--", linewidth=1.4)
    plt.xlabel("delta rho = after - before [arcsec]")
    plt.ylabel("Count")
    plt.title(f"{title} (1%-99% clipped)")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(out_png, dpi=180)
    plt.close()


def write_md(path: Path, lines: Iterable[str]) -> None:
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    ap.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    ap.add_argument("--output_root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    ap.add_argument("--run_tag", default=None)
    args = ap.parse_args()

    run_tag = args.run_tag or datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_utc")
    out_root = args.output_root / run_tag
    out_tables = out_root / "tables"
    out_figs = out_root / "figures"
    out_docs = out_root / "docs"
    out_meta = out_root / "meta"
    for p in [out_root, out_tables, out_figs, out_docs, out_meta]:
        p.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.input)
    for c in ["dRAcosDec_before_arcsec", "dDec_before_arcsec", "dRAcosDec_after_arcsec", "dDec_after_arcsec"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    if "catalog" in df.columns:
        df["catalog_norm"] = normalize_text_col(df["catalog"])
    else:
        df["catalog_norm"] = "unknown"
    if "center_of_frame" in df.columns:
        df["center_norm"] = normalize_text_col(df["center_of_frame"])
    else:
        df["center_norm"] = "unknown"
    df["gid"] = df["global_id"].astype(str).str.strip()

    paired = df[["dRAcosDec_before_arcsec", "dDec_before_arcsec", "dRAcosDec_after_arcsec", "dDec_after_arcsec"]].notna().all(axis=1)
    d = df[paired].copy()

    flagged_gids = set()
    if args.report.exists():
        rp = pd.read_csv(args.report)
        if "global_id" in rp.columns:
            flagged_gids = set(rp["global_id"].astype(str).str.strip())

    d["rho_before"] = np.hypot(d["dRAcosDec_before_arcsec"], d["dDec_before_arcsec"])
    d["rho_after"] = np.hypot(d["dRAcosDec_after_arcsec"], d["dDec_after_arcsec"])
    d["improved"] = d["rho_after"] < d["rho_before"]

    by_file = (
        d.groupby("gid", as_index=False)
        .agg(
            N=("gid", "size"),
            improve_rate=("improved", "mean"),
            med_before=("rho_before", "median"),
            med_after=("rho_after", "median"),
            p95_before=("rho_before", lambda x: np.percentile(x, 95)),
            p95_after=("rho_after", lambda x: np.percentile(x, 95)),
            catalog_mode=("catalog_norm", lambda x: x.mode().iloc[0] if len(x.mode()) else "unknown"),
            center_mode=("center_norm", lambda x: x.mode().iloc[0] if len(x.mode()) else "unknown"),
        )
        .sort_values(["N", "improve_rate"], ascending=[False, False])
    )
    by_file["med_improve_pct"] = safe_pct(by_file["med_before"], by_file["med_after"])
    by_file["p95_improve_pct"] = safe_pct(by_file["p95_before"], by_file["p95_after"])

    gids_ge30 = set(by_file.loc[by_file["N"] >= 30, "gid"].tolist())
    candidate_showcase = by_file[(by_file["N"] >= 200) & (by_file["improve_rate"] >= 0.60)].copy()
    showcase_gids = set(candidate_showcase.head(6)["gid"].tolist())

    scenarios: List[Scenario] = [
        Scenario("S0_full_paired", "All complete before/after pairs.", pd.Series(True, index=d.index), False),
        Scenario("S1_file_ge30", "Files with >=30 paired rows.", d["gid"].isin(gids_ge30), False),
        Scenario("S2_known_catalog", "Known catalog only.", d["catalog_norm"] != "unknown", False),
        Scenario(
            "S3_known_catalog_unflagged",
            "Known catalog and not listed in fallback report.",
            (d["catalog_norm"] != "unknown") & (~d["gid"].isin(flagged_gids)),
            False,
        ),
        Scenario(
            "S4_showcase_files",
            "Illustrative files with N>=200 and improve_rate>=0.60.",
            d["gid"].isin(showcase_gids),
            True,
        ),
    ]

    summary_rows = []
    for sc in scenarios:
        g = d[sc.mask].copy()
        if g.empty:
            continue
        row = metric_block(g)
        row["scenario"] = sc.name
        row["scenario_desc"] = sc.desc
        row["illustrative_only"] = sc.illustrative_only
        summary_rows.append(row)

        plot_cdf(g, f"{sc.name}: before vs after CDF", out_figs / f"{sc.name}_cdf.png")
        plot_delta_hist(g, f"{sc.name}: delta histogram", out_figs / f"{sc.name}_delta_hist.png")

    summary = pd.DataFrame(summary_rows)
    summary = summary.sort_values("p95_norm_improve_pct", ascending=False).reset_index(drop=True)

    summary.to_csv(out_tables / "scenario_summary.csv", index=False)
    by_file.to_csv(out_tables / "per_file_metrics.csv", index=False)
    candidate_showcase.to_csv(out_tables / "showcase_file_candidates.csv", index=False)

    if not candidate_showcase.empty:
        show = candidate_showcase.head(12).copy()
        x = np.arange(len(show))
        plt.figure(figsize=(10, 5))
        plt.bar(x - 0.2, show["improve_rate"].to_numpy(), width=0.4, label="improve_rate")
        plt.bar(x + 0.2, (show["med_improve_pct"] / 100.0).to_numpy(), width=0.4, label="med_improve_pct/100")
        plt.xticks(x, show["gid"].tolist(), rotation=45, ha="right")
        plt.ylabel("Rate")
        plt.title("Showcase file indicators")
        plt.grid(alpha=0.25, axis="y")
        plt.legend()
        plt.tight_layout()
        plt.savefig(out_figs / "showcase_files_bar.png", dpi=180)
        plt.close()

    def row_of(name: str) -> Dict[str, float]:
        t = summary[summary["scenario"] == name]
        return t.iloc[0].to_dict() if len(t) else {}

    full = row_of("S0_full_paired")
    top = summary.iloc[0].to_dict() if len(summary) else {}

    write_md(
        out_docs / "option_A_balanced.md",
        [
            "# Option A (Balanced)",
            "",
            "Main claim on S0 (full paired), robustness check with S1.",
            f"- Full paired N: {int(full.get('N', 0))}",
            f"- Improve rate (2D): {full.get('improve_rate_norm', np.nan):.4f}",
            f"- Median gain (%): {full.get('med_norm_improve_pct', np.nan):.3f}",
            f"- P95 gain (%): {full.get('p95_norm_improve_pct', np.nan):.3f}",
            "",
            "Messaging:",
            "- Robust metrics (median/P95) improve even when mean/RMS are tail-sensitive.",
            "- File-level stability is checked by S1.",
        ],
    )

    write_md(
        out_docs / "option_B_robust_metric_focus.md",
        [
            "# Option B (Robust Metric Focus)",
            "",
            "Use P95/median as primary indicators.",
            f"- Best scenario by P95 gain: {top.get('scenario', 'N/A')}",
            f"- P95 gain (%): {top.get('p95_norm_improve_pct', np.nan):.3f}",
            f"- Median gain (%): {top.get('med_norm_improve_pct', np.nan):.3f}",
            "",
            "Figures to use:",
            "- Scenario CDF",
            "- Delta histogram",
        ],
    )

    write_md(
        out_docs / "option_C_showcase_case_studies.md",
        [
            "# Option C (Showcase Cases)",
            "",
            "Illustrative supplement only, not the global headline.",
            f"- Showcase file count: {len(candidate_showcase)}",
            "- Selection rule: N>=200 and improve_rate>=0.60",
            "",
            "Candidate files:",
            *[f"- {gid}" for gid in candidate_showcase.head(10)["gid"].tolist()],
        ],
    )

    write_md(
        out_docs / "data_dictionary.md",
        [
            "# Data Dictionary",
            "",
            "Tables:",
            "- scenario_summary.csv",
            "- per_file_metrics.csv",
            "- showcase_file_candidates.csv",
            "",
            "Figures:",
            "- <scenario>_cdf.png",
            "- <scenario>_delta_hist.png",
            "- showcase_files_bar.png",
        ],
    )

    meta = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "input_file": str(args.input),
        "report_file": str(args.report),
        "total_rows": int(len(df)),
        "paired_rows": int(len(d)),
        "scenario_count": int(len(summary)),
        "showcase_file_count": int(len(candidate_showcase)),
    }
    (out_meta / "run_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print("Validation package generated:")
    print(out_root)


if __name__ == "__main__":
    main()
