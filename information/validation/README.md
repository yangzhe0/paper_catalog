# Validation Package

## Script
- `run_validation_analysis.py`

## Run
```bash
conda run --no-capture-output -n catalog python /data/sues01/Ancoj/validation/run_validation_analysis.py --run_tag run_YYYYMMDD_vX
```

## Output Structure
- `results/<run_tag>/tables/`
  - `scenario_summary.csv`
  - `per_file_metrics.csv`
  - `showcase_file_candidates.csv`
- `results/<run_tag>/figures/`
  - `<scenario>_cdf.png`
  - `<scenario>_delta_hist.png`
  - `showcase_files_bar.png`
- `results/<run_tag>/docs/`
  - `option_A_balanced.md`
  - `option_B_robust_metric_focus.md`
  - `option_C_showcase_case_studies.md`
  - `data_dictionary.md`
- `results/<run_tag>/meta/`
  - `run_meta.json`

## Scenario Notes
- `S0_full_paired`: all complete before/after pairs.
- `S1_file_ge30`: rows from files with at least 30 paired records.
- `S2_known_catalog`: known-catalog rows.
- `S3_known_catalog_unflagged`: known catalog and not listed in fallback report.
- `S4_showcase_files`: illustrative high-improvement files only.
