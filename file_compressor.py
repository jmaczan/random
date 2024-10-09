import os
import sys
import zipfile


def compress_files(pdf_path, jpg_dir, output_path):
    with zipfile.ZipFile(
        output_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9
    ) as zipf:
        # Add PDF
        zipf.write(pdf_path, os.path.basename(pdf_path))

        # Add JPGs
        for root, _, files in os.walk(jpg_dir):
            for file in files:
                if file.lower().endswith(".jpg"):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, jpg_dir)
                    zipf.write(file_path, arcname)


def main(pdf_path, jpg_dir, output_path):
    if not os.path.isfile(pdf_path):
        print(f"Error: {pdf_path} is not a valid file")
        sys.exit(1)

    if not os.path.isdir(jpg_dir):
        print(f"Error: {jpg_dir} is not a valid directory")
        sys.exit(1)

    compress_files(pdf_path, jpg_dir, output_path)
    print(f"Compression complete. Output file: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python script.py <pdf_path> <jpg_directory> [output_path]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    jpg_dir = sys.argv[2]
    output_path = sys.argv[3]

    main(pdf_path, jpg_dir, output_path)
