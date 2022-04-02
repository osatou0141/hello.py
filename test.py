import streamlit as st
import qrcode
from PIL import Image
st.title('QRコード生成')
url = st.text_input('URLの入力：')
if st.button('生成'):
    _img = qrcode.make(url)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
