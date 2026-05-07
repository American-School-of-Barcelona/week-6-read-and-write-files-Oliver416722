import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")
    
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    
    try:
        count = 0
        with open(filename, "r") as file:
            for line in file:
                stripped = line.lstrip()
                if stripped and not stripped.startswith("#"):
                    count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()