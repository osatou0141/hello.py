import streamlit as st
st.title('QRコード生成')
url = st.text_input('URLの入力：')
st.button('生成')
