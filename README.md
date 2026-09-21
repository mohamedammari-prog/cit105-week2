# CIT 105 Week 2 — QR Code Generator

This repository contains the CIT 105 Week 2 function library and QR Code Generator. The application supports both single QR code generation and batch generation from a CSV file.

## Run the application

1. Clone the repository.
2. Install the dependencies:
   `pip install -r requirements.txt`
3. Start Streamlit:
   `streamlit run app.py`
4. Open the local URL shown by Streamlit.

## Single Code Mode

Single Code mode accepts text or a URL, displays a QR code, and provides a PNG download. Image size, foreground color, and border width can be adjusted.

## Batch Mode

Batch from CSV mode accepts a CSV file with exactly these required columns:

- `name` — the name used to create the QR code filename.
- `url` — the HTTP or HTTPS URL encoded in the QR code.

Example:

```csv
name,url
Alice Smith,https://example.com/alice
Bob Smith,https://example.com/bob
```

The application previews the CSV before generating anything. It reports the number of valid and rejected rows and gives a reason for every rejected row.

Rows are rejected when:

- the CSV is missing the `name` or `url` column;
- the name is blank or contains only whitespace;
- the URL is blank or contains only whitespace;
- the URL is not an HTTP or HTTPS URL.

Valid rows are converted into QR code PNG files and packaged into one ZIP download. Filenames use the `safe_filename()` function from `functions.py`, and duplicate names receive a counter such as `Alice_Smith.png` and `Alice_Smith_2.png` instead of overwriting each other.

A sample file is included as `sample_batch.csv`. It contains both valid rows and rows that should be rejected.

## Functions

### 1. `celsius_to_fahrenheit(c)`

**Takes:** A Celsius temperature as a number.

**Returns:** The temperature converted to Fahrenheit.

**Rejects:** Non-numeric input with a `TypeError`.

### 2. `line_total(price, qty)`

**Takes:** A numeric price and a numeric quantity.

**Returns:** The price multiplied by the quantity.

**Rejects:** Non-numeric price or quantity and negative quantities.

### 3. `initials(full_name)`

**Takes:** A person's full name as a string.

**Returns:** The person's uppercase initials.

### 4. `is_valid_url(text)`

**Takes:** A possible URL.

**Returns:** `True` for HTTP or HTTPS URLs and `False` for invalid or blank input.

### 5. `truncate(text, limit=20)`

**Takes:** A string and an optional character limit.

**Returns:** The original or shortened text with an ellipsis when shortened.

### 6. `safe_filename(text)`

**Takes:** Arbitrary text.

**Returns:** Filename-safe text without spaces, slashes, or quotation marks.

## Project Files

- `functions.py` — reusable function library.
- `demo.py` — demonstrations of the function library.
- `app.py` — Streamlit QR Code Generator.
- `SPEC.md` — original application specification.
- `sample_batch.csv` — sample batch input.
- `requirements.txt` — application dependencies.

## AI Disclosure

GitHub Copilot was used as permitted by the assignment to assist with the code. The final code was reviewed and tested by the student.

## Batch Mode Update

Batch mode was developed on the `batch-mode` branch before being merged into `main`. The feature adds CSV preview, row validation, duplicate-safe filenames, and an in-memory ZIP download while preserving the existing single-code generation function.
