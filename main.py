import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
loaded_model= pickle.load(open("model.pkl", "rb"))
pred = st.file_uploader("upload csv files")
loaded_model.predict(pred)
submit = st.button("PREDICTION")
if submit:
    if 1 in pred:
        print("Fraud Detected")
    else:
            print("Transaction is geniune")
