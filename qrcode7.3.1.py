import qrcode
import streamlit as st
from PIL import Image

img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
img = Image.open("some_file.png")
st.image(img)
