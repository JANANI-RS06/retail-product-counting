import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("confidence_report.csv")

plt.figure(figsize=(9, 5))

bars = plt.bar(
    df["Image_Name"],
    df["mean"] * 100
)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.1f}%",
        ha="center",
        va="bottom"
    )

plt.title("Average Detection Confidence by Shelf Image")
plt.xlabel("Shelf Images")
plt.ylabel("Average Confidence (%)")
plt.ylim(0, 100)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig("confidence_comparison.png", dpi=150)
plt.show()

print("Confidence visualization saved!")