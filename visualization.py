import pandas as pd
import matplotlib.pyplot as plt

# Read stock reconciliation report
df = pd.read_csv("reconciliation_report.csv")

expected = int(df["Expected_Stock"].iloc[0])
detected = int(df["Detected_Stock"].iloc[0])
difference = int(df["Difference"].iloc[0])
status = df["Status"].iloc[0]

# Create dashboard with 3 charts
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1: Product count
axes[0].bar(
    ["Detected Products"],
    [detected]
)
axes[0].set_title("Total Product Count")
axes[0].set_ylabel("Number of Products")
axes[0].text(0, detected, str(detected), ha="center")

# Chart 2: Stock comparison
axes[1].bar(
    ["Expected", "Detected"],
    [expected, detected]
)
axes[1].set_title("Stock Comparison")
axes[1].set_ylabel("Stock Quantity")

# Chart 3: Stock difference
axes[2].bar(
    ["Difference"],
    [difference]
)
axes[2].set_title("Stock Difference")
axes[2].set_ylabel("Quantity Difference")

# Display stock status
fig.suptitle(
    f"Retail Stock Dashboard | Status: {status}",
    fontsize=15
)

plt.tight_layout()
plt.savefig("retail_dashboard.png", dpi=150)
plt.show()

print("Dashboard saved as retail_dashboard.png")