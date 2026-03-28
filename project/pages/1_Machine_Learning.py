import streamlit as st

st.title("Machine Learning Model")

st.write("## Data Preparation")
st.write("""
- ใช้ Breast Cancer Dataset
- ทำ normalization ด้วย StandardScaler
- แบ่ง train/test
""")

st.write("## Algorithms")
st.write("""
- Random Forest
- Gradient Boosting
- Logistic Regression
- Ensemble (Voting)
""")

st.write("## Development")
st.write("""
- Train โมเดล 3 ตัว
- รวมผลด้วย Voting
- Evaluate ด้วย Accuracy
""")

st.write("## Source")
st.write("UCI / Kaggle")
st.write("https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)")

st.markdown("---")
st.caption("Developed for Intelligent System Project")
