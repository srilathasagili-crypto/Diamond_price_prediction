import streamlit as st
import pandas as pd
import pickle

# ---------------------------
# Load trained pipeline safely
# ---------------------------
try:
    with open("diamond_pipeline.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f" Error loading model: {e}")
    st.stop()

# ---------------------------
# App Title
# ---------------------------
st.title(" Diamond Price Prediction")
st.markdown("Enter diamond details below:")

# ---------------------------
# User Inputs
# ---------------------------
carat = st.number_input("Carat", min_value=0.0, step=0.1)

cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])

color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])

clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

depth = st.number_input("Depth", min_value=0.0)

table = st.number_input("Table", min_value=0.0)

x = st.number_input("Length (x)", min_value=0.0)
y = st.number_input("Width (y)", min_value=0.0)
z = st.number_input("Height (z)", min_value=0.0)

# ---------------------------
# Prediction
# ---------------------------
if st.button("Predict Price"):

    # Input validation
    if carat <= 0 or x <= 0 or y <= 0 or z <= 0:
        st.error(" Please enter valid non-zero values for carat and dimensions.")
    
    else:
        try:
            # Create DataFrame (must match training features exactly)
            input_data = pd.DataFrame([{
                "carat": carat,
                "cut": cut,
                "color": color,
                "clarity": clarity,
                "depth": depth,
                "table": table,
                "x": x,
                "y": y,
                "z": z
            }])

            # Prediction
            prediction = model.predict(input_data)[0]

            # Output
            st.success(f" Predicted Price: ${round(prediction, 2)}")

        except Exception as e:
            st.error(f" Prediction failed: {e}")