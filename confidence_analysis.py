import pandas as pd

df = pd.read_csv("batch_results.csv")

summary = df.groupby("Image_Name")["Confidence"].agg(
    ["count", "mean", "min", "max"]
).round(3)

summary.to_csv("confidence_report.csv")

print("CONFIDENCE ANALYSIS REPORT")
print(summary)

print("\nReport saved as confidence_report.csv")