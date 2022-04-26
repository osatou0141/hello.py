import segno
import streamlit as st
from PIL import Image

QR_FILE = 'segnoQRcode.png'
qr_url = st.text_input('URLを入力', value='https://github.com/osatou0141/st_sample')

col1, col2 = st.columns(2)
with col1:
    version = st.slider('バージョン選択', 1, 15, value=5)
    correction = st.select_slider('誤り修正レベル', options=['L', 'M', 'Q', 'H'], value='H')

with col2:
    DARK_COLOR = st.selectbox('大ドットの色を選択', ['#000000', '#FFFFFF', '#FF0000', '#00FF00', '#0000FF'])
    CODE_COLOR = st.selectbox('ドットの色を選択', ['#000000', '#FFFFFF', '#FF0000', '#00FF00', '#0000FF'])
    BACK_COLOR = st.selectbox('背景の色を選択', ['#FFFFFF', '#000000', '#00FF00', '#FF0000', '#0000FF'])

qr = segno.make(qr_url, error=correction, version=version, mode='byte')
qr.save(QR_FILE, scale=5, dark=DARK_COLOR, data_dark=CODE_COLOR, data_light=BACK_COLOR)

img = Image.open(QR_FILE)
st.image(img)
