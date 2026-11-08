import subprocess
import sys

print("=" * 45)
print(" AI-BASED RETAIL PRODUCT COUNTING SYSTEM")
print("=" * 45)

print("\nSTEP 1: Running product detection...")

subprocess.run(
    [sys.executable, "retail_detection.py"],
    check=True
)

print("\nSTEP 2: Running stock reconciliation...")

subprocess.run(
    [sys.executable, "stock_reconciliation.py"],
    check=True
)

print("\nSTEP 3: Generating visual dashboard...")

subprocess.run(
    [sys.executable, "visualization.py"],
    check=True
)

print("\n" + "=" * 45)
print(" ALL PROJECT MODULES COMPLETED!")
print("=" * 45)