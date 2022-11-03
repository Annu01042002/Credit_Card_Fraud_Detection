 import pickle
loaded_model= pickle.load("model.pkl", "rb")
pred = st.file_uploader("upload csv files")
loaded_model.predict(pred)
submit = st.button("PREDICTION")
if submit:
    if 1 in pred:
        print("Fraud Detected")
    else:
            print("Transaction is geniune")
