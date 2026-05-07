import sys
from PIL import Image, ImageOps


def main():
    # Check number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check valid extensions (case‑insensitive)
    if not input_file.lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    if not output_file.lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    # Check that input and output have the same extension
    input_ext = input_file.lower().rsplit(".", 1)[1]
    output_ext = output_file.lower().rsplit(".", 1)[1]
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Open input (check if file exists)
    try:
        muppet = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open shirt and get its size
    shirt = Image.open("shirt.png")
    size = shirt.size

    # Resize and crop the muppet to match shirt size
    fitted_muppet = ImageOps.fit(muppet, size)

    # Overlay shirt on the fitted image
    fitted_muppet.paste(shirt, (0, 0), shirt)

    # Save the result
    fitted_muppet.save(output_file)


if __name__ == "__main__":
    main()