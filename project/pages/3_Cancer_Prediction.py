import streamlit as st
import joblib
import numpy as np
import os

st.title("Cancer Prediction")

model_path = os.path.join(os.path.dirname(__file__), "..", "cancer_model_v2.pkl")
model = joblib.load(model_path)

features = []

feature_names = [
    "mean radius","mean texture","mean perimeter","mean area","mean smoothness",
    "mean compactness","mean concavity","mean concave points","mean symmetry","mean fractal dimension"
]

st.subheader("Enter Patient Data")

for name in feature_names:
    val = st.number_input(name, min_value=0.0, value=0.0, step=1.0)
    features.append(val)

if st.button("Predict"):
    prediction = model.predict([features])

    if prediction[0] == 0:
        st.error("Malignant (Cancer)")
    else:
        st.success("Benign (Not Cancer)")

st.markdown("---")
st.caption("Developed for Intelligent System Project")
