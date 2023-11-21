rule prepare:
  output:
    "data/winequality.csv"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input:
    "data/winequality.csv"
  output:
    "profiling/report.html"
  shell:
    "python scripts/profile.py"

rule analyze:
  input:
    "data/winequality.csv"
  output:
    "results/summary_stats_and_regression_result.md",
    "results/plot.png"
  shell:
    "python scripts/analysis.py"