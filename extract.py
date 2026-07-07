import pdfplumber

pdf_path = "infosys-esg-report-2025-26.pdf"

all_text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            all_text += text + "\n"

print(all_text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("Extraction Completed")