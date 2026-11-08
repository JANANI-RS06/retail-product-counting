import pandas as pd
import matplotlib.pyplot as plt

# Read batch summary
df = pd.read_csv("batch_summary.csv")

# Create bar chart
plt.figure(figsize=(9, 5))

bars = plt.bar(
    df["Image_Name"],
    df["Total_Products"]
)

# Display count above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom"
    )

plt.title("Retail Product Detection - Batch Comparison")
plt.xlabel("Shelf Images")
plt.ylabel("Detected Product Count")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig("batch_comparison.png", dpi=150)
plt.show()

print("Batch comparison chart saved!")