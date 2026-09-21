import csv
import io
import zipfile

import qrcode
import streamlit as st

from functions import is_valid_url, safe_filename


MAX_LENGTH = 500


def generate_qr_image(text, size=300, foreground_color="black", border_width=4):
    
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
    
    stripped = text.strip()
    if stripped.startswith("http://") or stripped.startswith("https://"):
        without_protocol = stripped.split("://", 1)[1]
        if not without_protocol or " " in without_protocol:
            return True
    return False


def read_batch_csv(uploaded_file):
    
    raw_text = uploaded_file.getvalue().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(raw_text))

    if not reader.fieldnames:
        return [], ["CSV is empty or has no header row."]

    fieldnames = {field.strip() for field in reader.fieldnames if field}
    if "name" not in fieldnames or "url" not in fieldnames:
        return [], ['Missing required columns. CSV must contain "name" and "url".']

    valid_rows = []
    rejected = []

    for row_number, row in enumerate(reader, start=2):
        name = (row.get("name") or "").strip()
        url = (row.get("url") or "").strip()

        if not name and not url:
            rejected.append(f"Row {row_number}: name and URL are blank or whitespace.")
            continue
        if not name:
            rejected.append(f"Row {row_number}: name is blank or whitespace.")
            continue
        if not url:
            rejected.append(f"Row {row_number}: URL is blank or whitespace.")
            continue
        if not is_valid_url(url):
            rejected.append(f"Row {row_number}: URL is not a valid HTTP or HTTPS URL.")
            continue

        valid_rows.append({"name": name, "url": url})

    return valid_rows, rejected


def unique_filename(base_name, used_names):
    
    candidate = base_name
    counter = 2

    while candidate in used_names:
        candidate = f"{base_name}_{counter}"
        counter += 1

    used_names.add(candidate)
    return candidate


def build_batch_zip(rows, size=300, foreground_color="black", border_width=4):
    
    output = io.BytesIO()
    used_names = set()

    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for row in rows:
            image = generate_qr_image(
                row["url"],
                size=size,
                foreground_color=foreground_color,
                border_width=border_width,
            )

            filename_base = safe_filename(row["name"]).strip("._")
            if not filename_base:
                filename_base = "qr_code"

            filename_base = filename_base[:80]
            filename_base = unique_filename(filename_base, used_names)
            archive.writestr(f"{filename_base}.png", image.getvalue())

    output.seek(0)
    return output


st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="centered",
)

st.title("QR Code Generator")

mode = st.radio(
    "Mode",
    ["Single Code", "Batch from CSV"],
    horizontal=True,
)

if mode == "Single Code":
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

else:
    st.write("Upload a CSV with columns named name and url.")

    uploaded_file = st.file_uploader(
        "CSV file",
        type=["csv"],
    )

    size = st.slider(
        "Image Size",
        min_value=100,
        max_value=1000,
        value=300,
        step=50,
        key="batch_size",
    )

    foreground_color = st.color_picker(
        "Foreground Color",
        "#000000",
        key="batch_color",
    )

    border_width = st.slider(
        "Border Width",
        min_value=1,
        max_value=10,
        value=4,
        key="batch_border",
    )

    if uploaded_file is not None:
        try:
            valid_rows, rejected_rows = read_batch_csv(uploaded_file)
        except UnicodeDecodeError:
            valid_rows, rejected_rows = [], [
                "CSV could not be read as UTF-8 text."
            ]

        st.subheader("Batch Preview")
        st.write(f"**Valid rows:** {len(valid_rows)}")
        st.write(f"**Rejected rows:** {len(rejected_rows)}")

        if valid_rows:
            st.dataframe(valid_rows, use_container_width=True)

        if rejected_rows:
            st.write("**Rejected rows and reasons:**")
            for message in rejected_rows:
                st.warning(message)

        if valid_rows:
            generate_batch = st.button(
                "Generate ZIP",
                type="primary",
            )

            if generate_batch:
                zip_data = build_batch_zip(
                    valid_rows,
                    size=size,
                    foreground_color=foreground_color,
                    border_width=border_width,
                )

                st.download_button(
                    label="Download QR Codes ZIP",
                    data=zip_data.getvalue(),
                    file_name="qr_codes_batch.zip",
                    mime="application/zip",
                )
