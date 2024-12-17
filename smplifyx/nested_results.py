import os
import shutil

# Define the base directory containing the nested folder structure
base_dir = "OUTPUT_FINAL/images"

# Define the target directory where all images will be consolidated
output_dir = "OUTPUT_FINAL/walking_meshes"

# Create the target directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize a counter for duplicate filenames
file_counter = {}

# Walk through the directory structure
for root, dirs, files in os.walk(base_dir):
    # Check if the current folder is named '000'
    if os.path.basename(root) == "000":
        for file in files:
            # Check if the file is an image (adjust extensions as needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Construct the source file path
                source_path = os.path.join(root, file)

                # Handle duplicate filenames
                if file in file_counter:
                    # Increment the counter and create a new unique filename
                    file_counter[file] += 1
                    filename, ext = os.path.splitext(file)
                    unique_file = f"{filename}_{file_counter[file]}{ext}"
                else:
                    # Add the filename to the counter dictionary
                    file_counter[file] = 0
                    unique_file = file

                # Construct the destination file path
                destination_path = os.path.join(output_dir, unique_file)

                # Copy the file to the target directory
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} -> {destination_path}")

print("All images from '000' folders have been extracted to:", output_dir)
