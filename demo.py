import streamlit as st
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected Comedy.')
if genre == 'Drama':
    st.write('You selected Drama.')
if genre == 'Documentary':
    st.write('You selected Documentary')