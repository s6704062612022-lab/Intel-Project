import streamlit as st

st.set_page_config(page_title="Intelligent System Project", layout="wide")

st.markdown("# Intelligent System Project")
st.markdown("### Machine Learning & Neural Network Web App")
st.markdown("---")

st.write("""
Welcome to my project.

This web application uses:
- Machine Learning (Ensemble Model) to predict cancer risk
- Neural Network to analyze product review sentiment

Select a page from the sidebar to get started.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("## Cancer Prediction")
    st.write("""
    Predict whether a tumor is:
    - Malignant (Cancer)
    - Benign (Not cancer)
             
    Using an Ensemble Machine Learning model.
    """)
    st.page_link("pages/3_Cancer_Prediction.py", label="Go to Cancer Test", icon = "👉🏼")

with col2:
    st.markdown("## Review Sentiment")
    st.write("""
    Analyze product reviews:
    - Positive
    - Negative
             
    Using Neural Network (LSTM).
    """)
    st.page_link("pages/4_Product_Reviews.py", label="Go to Review Test", icon = "👉🏼")

st.markdown("---")

st.caption("Developed for Intelligent System Project")


