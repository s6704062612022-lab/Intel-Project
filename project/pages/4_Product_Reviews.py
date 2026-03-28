import streamlit as st
import joblib
from keras.models import load_model

st.title("Product Review")

model = load_model("../reviews_model.h5")
vectorizer = joblib.load("../tfidf_vectorizer.pkl")

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
