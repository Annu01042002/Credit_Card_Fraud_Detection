import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import streamlit as st

st.title("Credit Card Fraud Detection")
loaded_model= pickle.load(open("model.pkl", "rb"))
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# dataframe = pd.read_csv(uploaded_files,  encoding='utf-8')
# st.write(dataframe)
submit = st.button("PREDICTION")
if submit:
    st.sucess("ok")
#background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('')
