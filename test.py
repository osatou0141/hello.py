import streamlit as st
import pyqrcodeng as pyqrcode
from PIL import Image

st.title('QRコード生成')

QR_FILE = 'testQRcode.png'
url = st.text_input('URLを入力', value='https://github.com/osatou0141/st_sample')

col1, col2 = st.columns(2)
with col1:
    version = st.slider('バージョン選択', 1, 15, value=5)
    correction = st.select_slider('誤り修正レベル', options=['L', 'M', 'Q', 'H'], value='H')

with col2:
    CODE_COLOR = st.selectbox('ドットの色を選択', ['#000000', '#FFFFFF', '#FF0000', '#00FF00', '#0000FF'])
    BACK_COLOR = st.selectbox('背景の色を選択', ['#FFFFFF', '#000000', '#00FF00', '#FF0000', '#0000FF'])

qr = pyqrcode.create(url, correction, version)
qr.png('testQRcode.png', scale=5, module_color=CODE_COLOR, background=BACK_COLOR, quiet_zone=4)
img = Image.open(QR_FILE)
st.image(img)
