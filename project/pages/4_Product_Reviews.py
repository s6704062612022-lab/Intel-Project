import streamlit as st
import joblib
from pathlib import Path
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
st.title("Product Review")

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "reviews_model.pkl")
vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")

text = st.text_area("Enter review")

if st.button("Predict"):

    cleaned = clean_text(text)

    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)

    if pred[0] == 1:
        st.success("Positive")
    else:
        st.error("Negative")

st.markdown("---")
st.caption("Developed for Intelligent System Project")
