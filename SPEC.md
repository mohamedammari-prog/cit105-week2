```markdown
# QR Code Generator Specification

## Purpose

The QR Code Generator is a Streamlit web application that accepts text or a URL and creates a scannable QR code. The generated QR code is displayed on the page and can be downloaded as a PNG file.

## Input

The application accepts text or a URL from the user through a text box.

The maximum input length is 500 characters.

The application rejects empty input and input containing only whitespace. A clear error message is displayed instead of a traceback.

If the input appears to be a malformed URL, the application displays a warning but does not block the user from generating a QR code.

## Character Counter

A visible character counter displays the current number of characters entered and the maximum allowed length.

The counter uses the format:

`0 / 500 characters`

## QR Code Preview

After valid input is submitted, the generated QR code is displayed on the application page.

The QR code must be scannable using a phone camera.

## Download

The application provides a download button that allows the user to save the generated QR code as a PNG file.

The downloaded filename is derived from the user's input.

The application reuses the `safe_filename()` function from Assignment 1 to create the filename.

The filename is not a fixed name for every download.

## Image Size

The user can select the QR code image size.

The allowed range is 100 to 1000 pixels.

The default size is 300 pixels.

## Foreground Color

The user can select the QR code foreground color.

The default foreground color is black.

The application warns the user if a very light foreground color is selected because it may reduce QR code scanning reliability.

## Border Width

The user can select the QR code quiet-zone border.

The allowed range is 1 to 10 modules.

The default border width is 4 modules.

## QR Generation

The application uses the `qrcode` Python library with Pillow.

The generated image is created in memory using `io.BytesIO`.

The application does not write temporary PNG files to disk.

QR generation is contained in its own function.

The generation function accepts arguments and returns an image.

The generation function does not contain Streamlit calls.

## Dependencies

The application requires:

- Streamlit
- qrcode
- Pillow

All dependencies are listed in `requirements.txt`.

## Reuse

The application reuses `safe_filename()` from `functions.py` instead of creating a duplicate filename function.

## User Interface

The application contains:

- A text box for text or URLs.
- A visible character counter.
- An image-size control.
- A foreground-color control.
- A border-width control.
- A generate action.
- A QR code preview.
- A PNG download button.
- Clear error messages for empty and whitespace-only input.
- A warning for malformed-looking URLs.

## Testing

The application will be tested with:

1. Normal text.
2. A valid URL.
3. Empty input.
4. Whitespace-only input.
5. A malformed URL.
6. Long input.
7. Different image sizes.
8. Different foreground colors.
9. Different border widths.
10. Downloaded PNG files.
11. A phone camera to verify that generated QR codes scan correctly.

## AI Disclosure

AI assistance was used during development. The generated code was reviewed and tested by the student. AI-assisted work is identified in the commit history as required by the assignment.
```
