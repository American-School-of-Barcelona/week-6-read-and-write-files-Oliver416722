import sys

def main():
    # Check number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check if file ends in .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Try to open and read the file
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Count lines of code (ignore comments and blank lines)
    count = 0
    for line in lines:
        stripped = line.strip()
        # Ignore empty lines and lines that are comments
        if stripped == "" or stripped.startswith("#"):
            continue
        count += 1

    print(count)


if __name__ == "__main__":
    main()