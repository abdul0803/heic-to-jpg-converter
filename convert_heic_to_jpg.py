import os
from PIL import Image
import pillow_heif

source_folder =  "input file path"

destination_folder ="output file path"

os.makedirs(destination_folder, exist_ok=True)

for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".heic"):
        source_path = os.path.join(source_folder, file_name)
        
        heif_file = pillow_heif.read_heif(source_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )
        
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        destination_path = os.path.join(destination_folder, f"{os.path.splitext(file_name)[0]}.jpg")
        
        image.save(destination_path, "JPEG", quality=85)
        print(f"Converted: {file_name} -> {os.path.basename(destination_path)}")

print("Batch conversion completed.")
