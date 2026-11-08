import csv

# Expected stock count
expected_stock = int(input("Enter actual expected stock count: "))

# Read detected products from CSV
with open("product_counts.csv", "r") as file:
    reader = csv.DictReader(file)
    detected_products = list(reader)

# Calculate detected stock
detected_stock = len(detected_products)

# Calculate difference
difference = detected_stock - expected_stock

# Determine stock status
if difference > 0:
    status = "Over-count"
elif difference < 0:
    status = "Under-count"
else:
    status = "Matched"

# Display results
print("\n===== STOCK RECONCILIATION =====")
print("Expected Stock :", expected_stock)
print("Detected Stock :", detected_stock)
print("Difference     :", difference)
print("Stock Status   :", status)
# Save reconciliation report
with open("reconciliation_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Expected_Stock",
        "Detected_Stock",
        "Difference",
        "Status"
    ])

    writer.writerow([
        expected_stock,
        detected_stock,
        difference,
        status
    ])

print("Report saved as reconciliation_report.csv")

print("\nReconciliation completed!")