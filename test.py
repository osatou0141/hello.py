import streamlit as st
import qrcode
st.title('QRコード生成')
url = st.text_input('URLの入力：')
if st.button('生成'):
    img = qrcode.make(url)
    st.image(img)