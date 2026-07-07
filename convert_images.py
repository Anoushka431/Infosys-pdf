from PIL import Image
import os

input_folder = "images"
output_folder = "jpeg_images"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpx"):
        img_path = os.path.join(input_folder, filename)

        img = Image.open(img_path)
        rgb_img = img.convert("RGB")

        new_name = os.path.splitext(filename)[0] + ".jpg"
        rgb_img.save(os.path.join(output_folder, new_name), "JPEG")

        print(f"Converted: {new_name}")

print("All images converted successfully!")