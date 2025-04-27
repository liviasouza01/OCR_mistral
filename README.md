# Text Extraction with Mistral OCR

This document shows how to use the Mistral OCR API to extract text from PDF invoices and handwritten notes.

## Requirements

- Python 3.6+
- mistralai li
- Mistral API key

## Setup

1. Install the required dependencies:
   ```
   pip install mistralai
   ```

2. Configure your Mistral API key:
   - Create a `.env` file based on the `.env-example` 
   - Add your Mistral API key to the file

## Available Scripts

### 1. Invoice Text Extraction (nf_ingestion.py)

This script demonstrates how to extract specific information from a PDF invoice:
- Extracts the full text using OCR
- Identifies the invoice number and total amount using regular expressions
- Includes commented code to mask sensitive information (CPF, name, address)

Usage: 
```
python nf_ingestion.py
```

### 2. Handwritten Notes Text Extraction (handwritten_ingestion.py)

This script demonstrates how to extract text from a handwritten note:
- Extracts the full text using OCR
- Includes commented code to mask sensitive information (CPF, name, address)

Usge: 
```
python handwritten_ingestion.py
```  
