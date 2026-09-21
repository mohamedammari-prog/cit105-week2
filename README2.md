````markdown
# CIT 105 Week 2 — QR Code Generator

## Description

This project is a Streamlit QR Code Generator.

The application accepts text or a URL and generates a scannable QR code. The QR code is displayed on the page and can be downloaded as a PNG file.

The application allows the user to control:

- Image size from 100 to 1000 pixels
- Foreground color
- Border width from 1 to 10 modules

The application also validates empty and whitespace-only input and warns when an input appears to be a malformed URL.

## Files

### `functions.py`

Contains the reusable functions from the Function Library Exercise Set, including `safe_filename()`.

### `demo.py`

Demonstrates the functions from `functions.py`.

### `SPEC.md`

Contains the QR Code Generator specification created before the application code.

### `app.py`

Contains the Streamlit QR Code Generator application.

### `requirements.txt`

Contains the Python dependencies required to run the application.

## Requirements

- Python 3
- Streamlit
- qrcode
- Pillow

## Running the Application

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/cit105-week2.git
````

Enter the repository:

```bash
cd cit105-week2
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Streamlit will provide a local web address where the QR Code Generator can be used.

## How to Use

1. Enter text or a URL.
2. Check the character counter.
3. Select an image size.
4. Select a foreground color.
5. Select a border width.
6. Click **Generate QR Code**.
7. Scan the generated QR code with a phone camera.
8. Click **Download QR Code** to save the PNG.

## Validation

Empty input and whitespace-only input are rejected with a clear message.

Inputs that appear to be malformed URLs receive a warning but are still allowed as text.

## Image Generation

The QR generation logic is separated from the Streamlit interface.

The QR image is created in memory using `io.BytesIO`. No temporary PNG files are created.

The application uses the `qrcode` library with Pillow.

## AI Disclosure

AI assistance was used during development. The student reviewed and tested the code and is responsible for understanding the functions and application behavior.

AI-assisted work is identified in the commit history as required by the assignment.

## Screenshot

Add a screenshot of the running QR Code Generator here before submitting.

Example:

![QR Code Generator Screenshot](screenshot.png)

## Repository

Public GitHub repository:

`https://github.com/YOUR-USERNAME/cit105-week2`

```
```
