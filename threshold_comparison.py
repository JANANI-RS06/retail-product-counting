import pandas as pd

# Load both threshold results
df_025 = pd.read_csv("batch_results_025.csv")
df_040 = pd.read_csv("batch_results_040.csv")

# Count detections for each image
count_025 = df_025.groupby("Image_Name").size()
count_040 = df_040.groupby("Image_Name").size()

# Create comparison table
comparison = pd.DataFrame({
    "Threshold_0.25": count_025,
    "Threshold_0.40": count_040
}).fillna(0).astype(int)

comparison["Reduction"] = (
    comparison["Threshold_0.25"] -
    comparison["Threshold_0.40"]
)

comparison.loc["TOTAL"] = comparison.sum()

print("\nTHRESHOLD COMPARISON REPORT")
print(comparison)

# Save report
comparison.to_csv("threshold_comparison_report.csv")

print("\nReport saved as threshold_comparison_report.csv")