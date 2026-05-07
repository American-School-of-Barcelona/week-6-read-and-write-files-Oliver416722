import csv
import sys


def main():
    # Check number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check that both files are .csv
    if not input_file.endswith(".csv") or not output_file.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try to open and read the input CSV
    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                # Split name into last, first
                last, first = row["name"].split(", ")
                rows.append({
                    "first": first,
                    "last": last,
                    "house": row["house"],
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    # Write the new CSV with columns: first, last, house
    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()