import streamlit as st
from PIL import Image

st.set_page_config(page_title="NirogSathi", page_icon="🌱", layout="wide")
# st.title("NirogSathi")
image= Image.open("Nirog-Sathi-logo-final-bg-removed.png")
fingerPrint = Image.open("fingerprintLogo-removebg.png")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image)
    st.markdown("<h3 style='text-align: center; color: green; margin-top: -60px;'>Your Partner in Health and Happiness</h3>", unsafe_allow_html=True)
    st.image(fingerPrint,width=200)