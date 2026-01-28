"""
Minimal script to convert all images in a source folder to standardized RGB JPEG (.jpg) format.


Features:
- Converts PNG, JPG, JPEG, JFIF images to RGB JPG.
- Saves all converted images in a destination folder `cleaned_receipts`.
- Preserves original filenames.
- Creates destination folder automatically if it doesn't exist.
- Logs any errors during conversion.


Usage:
1. Set `source_folder` to your images folder.
2. Run the script.
3. All converted images will be in `cleaned_receipts`.
"""

from PIL import Image
import os

# Current working directory
cwd = os.getcwd()

# Source folder (all receipts in one place)
source_folder = r"C:\Users\Asus\Downloads\source"

# Destination folder (created in same folder)
dest_folder = os.path.join(cwd, "cleaned_receipts")
os.makedirs(dest_folder, exist_ok=True)

# Conversion loop
for filename in os.listdir(source_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".jfif")):
        try:
            img_path = os.path.join(source_folder, filename)
            img = Image.open(img_path).convert("RGB")
            base_name = os.path.splitext(filename)[0]
            save_path = os.path.join(dest_folder, f"{base_name}.jpg")
            img.save(save_path, "JPEG", quality=95)
        except Exception as e:
            print(f"Error converting {filename}: {e}")

print("Conversion complete! All images saved in:", dest_folder)