rule step1:
  output:
    "./data/wine+quality.zip",
    "./data/winequality-red.csv",
    "./data/winequality-white.csv",
    "./data/winequality.names",
  shell:
    "python ./scripts/prepare_data.py"

rule step2:
  output:
    "./data/winequality.csv"
    "./profiling/report.html"
  shell:
    "python ./scripts/profile.py"

rule step3:
  input:
    "./data/winequality.csv"
  output:
    "./results/model_accuracy.txt"
    "./results/plot.png"
  shell:
    "python ./scripts/analyze.py"