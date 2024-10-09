import os
import sys
from PIL import Image


def process_image(file_path, output_dir):
    with Image.open(file_path) as img:
        # Convert to RGB if it's not already (handles PNG with transparency)
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Get the longer side
        max_size = max(img.size)

        # If longer side is more than 1600px, resize
        if max_size > 1600:
            ratio = 1600 / max_size
            new_size = tuple(int(x * ratio) for x in img.size)
            img = img.resize(new_size, Image.LANCZOS)

        # If longer side is less than 1600px, print info
        elif max_size < 1600:
            print(
                f"Image {file_path} has longer side less than 1600px. Size: {img.size}"
            )

        # Save as JPG in the output directory
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        new_path = os.path.join(output_dir, f"{base_name}.jpg")
        img.save(new_path, "JPEG", quality=95)
        print(f"Processed image saved: {new_path}")


def main(input_directory, output_directory):
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(input_directory, filename)
            process_image(file_path, output_directory)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_directory> <output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.isdir(input_directory):
        print(f"Error: {input_directory} is not a valid directory")
        sys.exit(1)

    main(input_directory, output_directory)
