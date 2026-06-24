import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("diamond.pkl")

st.title("💎 Diamond Price Prediction")

# Inputs
carat = st.number_input("Carat", min_value=0.0)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)
depth = st.number_input("Depth")
table = st.number_input("Table")
x = st.number_input("X")
y = st.number_input("Y")
z = st.number_input("Z")

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "carat": [carat],
        "cut": [cut],
        "color": [color],
        "clarity": [clarity],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Diamond Price: ${prediction:.2f}")