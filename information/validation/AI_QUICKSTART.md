# AI Quickstart (Validation)

## 1) Goal
This folder is a ready-to-run validation workspace for ephemeris debiasing analysis.

## 2) Input (main table)
- `validation/input/absolute_03_correction.csv`

## 3) Environment
Use conda env `catalog`:
```bash
conda run --no-capture-output -n catalog python ...
```

## 4) Main scripts
- `validation/run_validation_analysis.py`
  - Generates baseline scenarios (S0-S4), tables, figures, and docs.
- `validation/generate_breakdowns.py`
  - Generates subgroup breakdowns by target/observatory/epoch.

## 5) Typical run sequence
```bash
conda run --no-capture-output -n catalog python /data/sues01/Ancoj/validation/run_validation_analysis.py --input /data/sues01/Ancoj/validation/input/absolute_03_correction.csv --run_tag run_xxx

conda run --no-capture-output -n catalog python /data/sues01/Ancoj/validation/generate_breakdowns.py --input /data/sues01/Ancoj/validation/input/absolute_03_correction.csv --output_dir /data/sues01/Ancoj/validation/results/run_xxx
```

## 6) Output location
- `validation/results/<run_tag>/tables`
- `validation/results/<run_tag>/figures`
- `validation/results/<run_tag>/docs`
- `validation/results/<run_tag>/meta`

## 7) Fast orientation for a new AI
1. Read `validation/README.md`.
2. Open `validation/results/<latest_run>/tables/scenario_summary.csv`.
3. Open `validation/results/<latest_run>/docs/option_A_balanced.md` and `option_D_subgroup_focus.md`.
4. Pick a reporting strategy, then refine figures/tables as needed.
