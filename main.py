import streamlit as st
from PIL import Image
import pickle as pkl

class_list = {'0': 'Normal', '0': 'Pneumonia'}

st.title('Pneumonia Detection')

input = open('model_1.pkl', 'rb')
model = pkl.load(input)

st.header('Upload image')
image = st.file_uploader('Choose an image', type={['png', 'jpg', 'jpeg']})
                         
if image is not None:
  image = Image.open(image)
  st.image(image, caption='Test image')
