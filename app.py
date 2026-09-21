```python
import io

import qrcode
import streamlit as st

from functions import safe_filename


MAX_LENGTH = 500


def generate_qr_image(text, size=300, foreground_color="black", border_width=4):
    """Generate a QR code image in memory and return it."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=border_width,
    )

    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color=foreground_color,
        back_color="white",
    ).convert("RGB")

    image.thumbnail((size, size))

    output = io.BytesIO()
    image.save(output, format="PNG")
    output.seek(0)

    return output


def looks_like_malformed_url(text):
    """Return True when text appears to be a malformed HTTP or HTTPS URL."""
    stripped = text.strip()

    if stripped.startswith("http://") or stripped.startswith("https://"):
        without_protocol = stripped.split("://", 1)[1]

        if not without_protocol or " " in without_protocol:
            return True

    return False


st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="centered",
)

st.title("QR Code Generator")
st.write("Enter text or a URL to create a downloadable QR code.")

text = st.text_area(
    "Text or URL",
    max_chars=MAX_LENGTH,
    height=120,
    placeholder="Enter text or a URL here...",
)

st.caption(f"{len(text)} / {MAX_LENGTH} characters")

size = st.slider(
    "Image Size",
    min_value=100,
    max_value=1000,
    value=300,
    step=50,
)

foreground_color = st.color_picker(
    "Foreground Color",
    "#000000",
)

border_width = st.slider(
    "Border Width",
    min_value=1,
    max_value=10,
    value=4,
)

generate = st.button("Generate QR Code", type="primary")

if generate:
    if not text.strip():
        st.error("Please enter some text or a URL.")
    elif looks_like_malformed_url(text):
        st.warning(
            "This input looks like a malformed URL. "
            "It will still be treated as text."
        )

    if text.strip():
        qr_data = generate_qr_image(
            text.strip(),
            size=size,
            foreground_color=foreground_color,
            border_width=border_width,
        )

        st.image(qr_data, caption="Generated QR Code")

        filename_base = safe_filename(text.strip())

        if not filename_base:
            filename_base = "qr_code"

        filename = f"{filename_base[:80]}.png"

        st.download_button(
            label="Download QR Code",
            data=qr_data.getvalue(),
            file_name=filename,
            mime="image/png",
        )
```
