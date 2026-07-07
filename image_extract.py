import fitz
import os

pdf_path = "infosys-esg-report-2025-26.pdf"


output_folder = "images"
os.makedirs(output_folder, exist_ok=True)

doc = fitz.open(pdf_path)

image_count = 0

for page_number in range(len(doc)):
    page = doc.load_page(page_number)

    images = page.get_images(full=True)

    for img_index, img in enumerate(images):

        xref = img[0]

        base_image = doc.extract_image(xref)

        image_bytes = base_image["image"]

        image_ext = base_image["ext"]

        image_name = f"page{page_number+1}_image{img_index+1}.{image_ext}"

        image_path = os.path.join(output_folder, image_name)

        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)

        print(f"Saved: {image_name}")

        image_count += 1

print(f"\nTotal Images Extracted: {image_count}")