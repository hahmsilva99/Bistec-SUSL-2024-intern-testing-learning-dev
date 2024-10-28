import streamlit as st
from PIL import Image, ImageEnhance
from PIL.ImageFilter import *
import io

# Create a title for the app
st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("--")

# File uploader to upload images (jpg, png, jpeg)
image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

# Placeholder for image details
info = st.empty()
size = st.empty()
mode = st.empty()
format = st.empty()

# If an image is uploaded, display its details and allow for editing
if image:
    # Open the image using PIL
    img = Image.open(image)

    # Display basic image information
    info.markdown("<h2 style='text-align: center;'>Information</h2>", unsafe_allow_html=True)
    size.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    format.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html=True)

    # Image resizing section
    st.markdown("<h2 style='text-align: center;'>Resizing</h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)

    # Image rotation section
    st.markdown("<h2 style='text-align: center;'>Rotation</h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree")

    # Image cropping section
    st.markdown("<h2 style='text-align: center;'>Cropping</h2>", unsafe_allow_html=True)
    left = st.number_input("Left", min_value=0, max_value=img.width, value=0)
    top = st.number_input("Top", min_value=0, max_value=img.height, value=0)
    right = st.number_input("Right", min_value=left, max_value=img.width, value=img.width)
    bottom = st.number_input("Bottom", min_value=top, max_value=img.height, value=img.height)

    # Brightness and contrast section
    st.markdown("<h2 style='text-align: center;'>Brightness & Contrast</h2>", unsafe_allow_html=True)
    brightness = st.slider("Brightness", 0.5, 2.0, 1.0)  # Default is 1.0 (no change)
    contrast = st.slider("Contrast", 0.5, 2.0, 1.0)  # Default is 1.0 (no change)

    # Filters section
    st.markdown("<h2 style='text-align: center;'>Filters</h2>", unsafe_allow_html=True)
    filters = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss", "Smooth"))

    # Button to apply changes
    s_btn = st.button("Submit")

    if s_btn:
        # Resize, rotate, and crop the image
        edited = img.resize((width, height)).rotate(degree)

        # Apply cropping
        cropped_img = edited.crop((left, top, right, bottom))

        # Apply brightness and contrast enhancements
        enhancer_brightness = ImageEnhance.Brightness(cropped_img)
        enhanced_img = enhancer_brightness.enhance(brightness)

        enhancer_contrast = ImageEnhance.Contrast(enhanced_img)
        enhanced_img = enhancer_contrast.enhance(contrast)

        # Display the edited image
        st.image(enhanced_img)

        # Apply filters
        if filters != "None":
            if filters == "Blur":
                filtered = enhanced_img.filter(BLUR)
            elif filters == "Detail":
                filtered = enhanced_img.filter(DETAIL)
            elif filters == "Emboss":
                filtered = enhanced_img.filter(EMBOSS)
            else:
                filtered = enhanced_img.filter(SMOOTH)
            st.image(filtered)

        # Add save button to allow the user to download the edited image
        buf = io.BytesIO()
        enhanced_img.save(buf, format='PNG')
        byte_im = buf.getvalue()

        st.download_button(
            label="Download edited image",
            data=byte_im,
            file_name="edited_image.png",
            mime="image/png"
        )
