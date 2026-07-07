import pdfplumber
import pandas as pd

pdf_path = "infosys-esg-report-2025-26.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page_no, page in enumerate(pdf.pages):

        tables = page.extract_tables()

        for i, table in enumerate(tables):

            df = pd.DataFrame(table)

            df.to_csv(
                f"table_page{page_no+1}_{i+1}.csv",
                index=False
            )

print("Tables Extracted")