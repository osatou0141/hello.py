import segno
import streamlit as st
from PIL import Image
segno_QRFILE = 'qrcode.png'
qrcode = segno.make('Rain')
qrcode.save('qrcode.png')
img = Image.open(segno_QRFILE)
st.image(img)
