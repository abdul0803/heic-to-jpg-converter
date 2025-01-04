from PIL import Image
import pillow_heif

# Read the HEIC file
heif_file = pillow_heif.read_heif("HEIC_file.HEIC")

# Convert HEIC to a Pillow Image object
image = Image.frombytes(
    heif_file.mode,
    heif_file.size,
    heif_file.data,
    "raw",
)

# Save the image as JPG
image.save("./picture_name85.jpg", "JPEG", quality=85)
image.save("./picture_name52.jpg", "JPEG", quality=50)

