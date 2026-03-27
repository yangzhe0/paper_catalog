#!/usr/bin/env python3
"""Generate subgroup breakdown tables/figures for validation v2."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def safe_pct(before, after):
    b = np.asarray(before, dtype=float)
    a = np.asarray(after, dtype=float)
    out = np.full(np.shape(b), np.nan, dtype=float)
    valid = np.isfinite(b) & np.isfinite(a) & (b != 0)
    out[valid] = (b[valid] - a[valid]) / b[valid] * 100.0
    if out.shape == ():
        return float(out)
    return out


def add_metrics(grouped: pd.core.groupby.generic.DataFrameGroupBy, key_name: str) -> pd.DataFrame:
    rows = []
    for key, g in grouped:
        b = np.hypot(g["dRAcosDec_before_arcsec"].to_numpy(dtype=float), g["dDec_before_arcsec"].to_numpy(dtype=float))
        a = np.hypot(g["dRAcosDec_after_arcsec"].to_numpy(dtype=float), g["dDec_after_arcsec"].to_numpy(dtype=float))
        row = {
            key_name: key,
            "N": int(len(g)),
            "improve_rate": float(np.mean(a < b)),
            "med_before": float(np.median(b)),
            "med_after": float(np.median(a)),
            "med_improve_pct": float(safe_pct(np.median(b), np.median(a))),
            "p95_before": float(np.percentile(b, 95)),
            "p95_after": float(np.percentile(a, 95)),
            "p95_improve_pct": float(safe_pct(np.percentile(b, 95), np.percentile(a, 95))),
        }
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="/data/sues01/Ancoj/result/absolute_03_correction.csv")
    ap.add_argument("--output_dir", required=True)
    ap.add_argument("--min_n_obs", type=int, default=50)
    ap.add_argument("--min_n_target", type=int, default=80)
    args = ap.parse_args()

    out_dir = Path(args.output_dir)
    out_tables = out_dir / "tables"
    out_figs = out_dir / "figures"
    out_docs = out_dir / "docs"
    out_tables.mkdir(parents=True, exist_ok=True)
    out_figs.mkdir(parents=True, exist_ok=True)
    out_docs.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.input)
    for c in ["dRAcosDec_before_arcsec", "dDec_before_arcsec", "dRAcosDec_after_arcsec", "dDec_after_arcsec"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    paired = df[["dRAcosDec_before_arcsec", "dDec_before_arcsec", "dRAcosDec_after_arcsec", "dDec_after_arcsec"]].notna().all(axis=1)
    d = df[paired].copy()

    d["target_norm"] = d["target_name"].fillna("unknown").astype(str).str.strip()
    d["obs_norm"] = d["observatory"].fillna("unknown").astype(str).str.strip()

    # target breakdown
    t = add_metrics(d.groupby("target_norm"), "target")
    t = t.sort_values(["N", "improve_rate"], ascending=[False, False]).reset_index(drop=True)
    t.to_csv(out_tables / "by_target_metrics.csv", index=False)

    t_plot = t[t["N"] >= args.min_n_target].head(12).copy()
    if len(t_plot):
        x = np.arange(len(t_plot))
        plt.figure(figsize=(10, 5))
        plt.bar(x - 0.2, t_plot["improve_rate"].to_numpy(), width=0.4, label="improve_rate")
        plt.bar(x + 0.2, (t_plot["med_improve_pct"] / 100.0).to_numpy(), width=0.4, label="med_improve_pct/100")
        plt.xticks(x, t_plot["target"].tolist(), rotation=45, ha="right")
        plt.ylabel("Rate")
        plt.title("Top targets by sample size: improvement indicators")
        plt.grid(alpha=0.25, axis="y")
        plt.legend()
        plt.tight_layout()
        plt.savefig(out_figs / "target_top12_improve_rate.png", dpi=180)
        plt.close()

    # observatory breakdown
    o = add_metrics(d.groupby("obs_norm"), "observatory")
    o = o.sort_values(["N", "improve_rate"], ascending=[False, False]).reset_index(drop=True)
    o.to_csv(out_tables / "by_observatory_metrics.csv", index=False)

    o_plot = o[o["N"] >= args.min_n_obs].head(12).copy()
    if len(o_plot):
        x = np.arange(len(o_plot))
        plt.figure(figsize=(10, 5))
        plt.bar(x - 0.2, o_plot["improve_rate"].to_numpy(), width=0.4, label="improve_rate")
        plt.bar(x + 0.2, (o_plot["med_improve_pct"] / 100.0).to_numpy(), width=0.4, label="med_improve_pct/100")
        plt.xticks(x, o_plot["observatory"].tolist(), rotation=45, ha="right")
        plt.ylabel("Rate")
        plt.title("Top observatories by sample size: improvement indicators")
        plt.grid(alpha=0.25, axis="y")
        plt.legend()
        plt.tight_layout()
        plt.savefig(out_figs / "observatory_top12_improve_rate.png", dpi=180)
        plt.close()

    # epoch (2-year bins)
    if "jd_tt" in d.columns:
        jd = pd.to_numeric(d["jd_tt"], errors="coerce")
    else:
        jd = pd.to_numeric(d["jd"], errors="coerce")
    year = 2000.0 + (jd - 2451545.0) / 365.25
    d["year"] = year

    y_min = int(np.floor(np.nanmin(year)))
    y_max = int(np.ceil(np.nanmax(year)))
    bins = np.arange(y_min, y_max + 2, 2)
    if len(bins) < 3:
        bins = np.array([y_min, y_min + 2, y_min + 4])
    d["year_bin"] = pd.cut(d["year"], bins=bins, include_lowest=True)

    y_rows = []
    for label, g in d.groupby("year_bin"):
        if len(g) == 0:
            continue
        b = np.hypot(g["dRAcosDec_before_arcsec"].to_numpy(dtype=float), g["dDec_before_arcsec"].to_numpy(dtype=float))
        a = np.hypot(g["dRAcosDec_after_arcsec"].to_numpy(dtype=float), g["dDec_after_arcsec"].to_numpy(dtype=float))
        y_rows.append(
            {
                "year_bin": str(label),
                "N": int(len(g)),
                "med_before": float(np.median(b)),
                "med_after": float(np.median(a)),
                "improve_rate": float(np.mean(a < b)),
                "med_improve_pct": float(safe_pct(np.median(b), np.median(a))),
            }
        )
    y = pd.DataFrame(y_rows)
    y.to_csv(out_tables / "by_epoch2y_metrics.csv", index=False)

    if len(y):
        yy = y[y["N"] >= 30].copy().reset_index(drop=True)
        if len(yy):
            x = np.arange(len(yy))
            plt.figure(figsize=(12, 5))
            plt.plot(x, yy["med_before"].to_numpy(), marker="o", label="med_before")
            plt.plot(x, yy["med_after"].to_numpy(), marker="o", label="med_after")
            plt.xticks(x, yy["year_bin"].tolist(), rotation=45, ha="right")
            plt.ylabel("Median residual norm [arcsec]")
            plt.title("Epoch trend (2-year bins)")
            plt.grid(alpha=0.25)
            plt.legend()
            plt.tight_layout()
            plt.savefig(out_figs / "epoch2y_median_trend.png", dpi=180)
            plt.close()

    lines = [
        "# Option D (Subgroup Emphasis)",
        "",
        "Focus on subgroup heterogeneity: target / observatory / epoch bins.",
        "",
        "Generated tables:",
        "- by_target_metrics.csv",
        "- by_observatory_metrics.csv",
        "- by_epoch2y_metrics.csv",
        "",
        "Generated figures:",
        "- target_top12_improve_rate.png",
        "- observatory_top12_improve_rate.png",
        "- epoch2y_median_trend.png",
    ]
    (out_docs / "option_D_subgroup_focus.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("Breakdowns generated:")
    print(out_dir)


if __name__ == "__main__":
    main()
