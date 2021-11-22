import streamlit as st
from PIL import Image

st.title('Image Viewer')

files = st.file_uploader("Choose some images", accept_multiple_files=True)

for file in files:
  im = Image.open(file)
  capt = f'{str(im.size[0])}, {str(im.size[1])}({im.format}, {im.mode})'
  st.subheader(file.name)
  st.image(im, caption=capt, use_column_width=True)
