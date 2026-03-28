import streamlit as st
import joblib
from tensorflow.keras.models import load_model
import os

st.title("Product Review")

model_path = os.path.join(os.path.dirname(__file__), "..", "reviews_model.h5")
vectorizer_path = os.path.join(os.path.dirname(__file__), "..", "tfidf_vectorizer.pkl")

model = load_model(model_path)
vectorizer = joblib.load(vectorizer_path)

text = st.text_area("Enter review")

if st.button("Predict"):
    vec = vectorizer.transform([text]).toarray()
    pred = model.predict(vec)

    if pred[0][0] > 0.5:
        st.success("Positive")
    else:
        st.error("Negative")

st.markdown("---")
st.caption("Developed for Intelligent System Project")
