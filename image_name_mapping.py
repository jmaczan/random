import sys
import os
import shutil

FILENAME_MAPPING = {}


def copy_and_rename(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            src_path = os.path.join(input_dir, filename)
            new_name = FILENAME_MAPPING.get(
                filename, filename
            )  # Use original name if not in mapping
            dst_path = os.path.join(output_dir, new_name)
            shutil.copy2(src_path, dst_path)
            print(f"Copied and renamed: {filename} -> {new_name}")


def main(input_dir, output_dir):
    copy_and_rename(input_dir, output_dir)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_directory> <output_directory>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isdir(input_dir):
        print(f"Error: {input_dir} is not a valid directory")
        sys.exit(1)

    main(input_dir, output_dir)
