import segno
import streamlit as st
from PIL import Image
qrcode = segno.make('Yellow Submarine')
qrcode.save('yellow-submarine.png')
img = Image.open('yellow-submarine.png')
st.image(img)
