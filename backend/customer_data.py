import csv
from pathlib import Path

def read_customers():
    csv_path = Path(__file__).resolve().parent.parent / "data" / "customers.csv"
    csv_path.parent.mkdir(exist_ok=True)  # make sure 'data' folder exists

    # Auto-create if file missing
    if not csv_path.exists():
        with open(csv_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["CustomerID", "Name", "Email", "City"])
            writer.writerow([1, "Alice", "alice@example.com", "New York"])
            writer.writerow([2, "Bob", "bob@example.com", "London"])
            writer.writerow([3, "Charlie", "charlie@example.com", "Sydney"])

    customers = []
    with open(csv_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)

    return customers
