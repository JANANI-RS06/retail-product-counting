import pandas as pd

# Read batch detection results
df = pd.read_csv("batch_results.csv")

# Calculate summary for each image
summary = df.groupby("Image_Name").agg(
    Total_Products=("Product_ID", "count"),
    Average_Confidence=("Confidence", "mean")
).reset_index()

summary["Average_Confidence"] = (
    summary["Average_Confidence"].round(3)
)

# Display summary
print("\n===== BATCH DETECTION SUMMARY =====")
print(summary.to_string(index=False))

# Save summary
summary.to_csv("batch_summary.csv", index=False)

print("\nTotal Images:", len(summary))
print("Total Products:", summary["Total_Products"].sum())
print("Summary saved as batch_summary.csv")