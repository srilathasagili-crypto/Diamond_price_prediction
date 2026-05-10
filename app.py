import streamlit as st
import pickle
import numpy as np

# load model
model = pickle.load(open("diamond_pipeline.pkl", "rb"))

st.title("Diamond Price Prediction 💎")

# inputs
carat = st.number_input("Carat")
depth = st.number_input("Depth")

# prediction
if st.button("Predict"):
    input_data = np.array([[carat, depth]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]}")