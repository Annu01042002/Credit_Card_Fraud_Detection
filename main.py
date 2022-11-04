import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import streamlit as st

loaded_model= pickle.load(open("model.pkl", "rb"))
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
dataframe = pd.read_csv(uploaded_files)
st.write(dataframe)
submit = st.button("PREDICTION")
if submit:
    st.sucess("ok")
