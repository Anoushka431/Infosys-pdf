
# **Infosys ESG Report PDF Content Extraction**

A Python-based project for extracting textual content, tables, and embedded images from the **Infosys ESG Report PDF**. The project processes the PDF and generates structured outputs including text files, CSV tables, and extracted images for further analysis and document processing.

---

## Features

* PDF text extraction
* Table extraction from PDF documents
* Embedded image extraction
* Conversion of extracted JPX images into JPEG format
* Structured output generation
* CSV export for extracted tables
* Organized storage of extracted images
* Simple and modular Python scripts

---

## Project Workflow

```
Infosys ESG Report PDF
          │
          ▼
Document Extraction
(Text, Tables, Images)
          │
          ▼
Text Output (output.txt)
          │
          ├────────► Tables (CSV Files)
          │
          └────────► Images (JPX)
                         │
                         ▼
                JPEG Image Conversion
```

---

## Project Structure

```
INFOSYS_PDF_EXTRACTION/
│
├── extract.py
├── table_extract.py
├── image_extract.py
├── convert_images.py
│
├── output.txt
├── requirements.txt
├── README.md
├── TECH_STACK.md
├── AI_USAGE.md
├── .gitignore
│
├── images/
│
├── jpeg_images/
│
└── table_page*.csv
```

---

## Technologies Used

### Programming Language

* Python 3.12

### Libraries

* pdfplumber
* PyMuPDF (fitz)
* Pandas
* Pillow
* os

### Development Tools

* Visual Studio Code
* Git
* GitHub
* pip

---

## Installation

Clone the Repository

```bash
git clone https://github.com/Anoushka431/Infosys-pdf.git

cd Infosys-PDF-Extraction
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1 – Extract Text

```bash
python extract.py
```

This generates:

* `output.txt`

---

### Step 2 – Extract Tables

```bash
python table_extract.py
```

This generates:

* `table_page1_1.csv`
* `table_page2_1.csv`
* ...

---

### Step 3 – Extract Images

```bash
python image_extract.py
```

This generates:

* `images/`

---

### Step 4 – Convert Images to JPEG

```bash
python convert_images.py
```

This generates:

* `jpeg_images/`

---

## Dataset

The project uses the **Infosys ESG Report PDF** as the source document.

The dataset includes:

* Textual content
* Tables
* Embedded images

---

## AI Usage

AI was used as a learning and development assistant for:

* Understanding PDF extraction techniques
* Understanding Python libraries such as pdfplumber, PyMuPDF, Pandas, and Pillow
* Debugging Python errors
* Preparing project documentation
* Git and GitHub guidance

Further details are available in **AI_USAGE.md**.

---

## Future Improvements

* Automatic extraction of document metadata
* OCR support for scanned PDF documents
* Export extracted content into JSON format
* Improved table detection for complex layouts
* Batch processing of multiple PDF documents

---

## Author

**Anoushka Koley**

GitHub: **[https://github.com/Anoushka431](https://github.com/Anoushka431)**

**Project:** *Infosys ESG Report PDF Content Extraction*




