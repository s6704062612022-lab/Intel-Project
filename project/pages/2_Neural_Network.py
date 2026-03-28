import streamlit as st

st.title("Neural Network Model")

st.write("## Data Preparation")
st.write("""
- ใช้ IMDB Dataset
- clean text
- แปลงเป็น TF-IDF
""")

st.write("## Neural Network")
st.write("""
- Input Layer
- Hidden Layer (ReLU)
- Output Layer (Sigmoid)
""")

st.write("## Development")
st.write("""
- Train Neural Network
- ใช้ Binary Classification
""")

st.write("## Source")
st.write("Kaggle IMDB Dataset")
st.write("https://ai.stanford.edu/~amaas/data/sentiment/")

st.markdown("---")
st.caption("Developed for Intelligent System Project")
