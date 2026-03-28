from pathlib import Path
import streamlit as st
import joblib

st.title("Product Review")

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "reviews_model.pkl")
vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")

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
