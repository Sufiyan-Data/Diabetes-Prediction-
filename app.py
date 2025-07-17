import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("diabetes_model.pkl")

# Page title
st.title("Diabetes Prediction App")
st.write("Enter patient details to predict diabetes risk:")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300)
bp = st.number_input("Blood Pressure", min_value=0, max_value=200)
skinthickness = st.number_input("Skin Thickness", min_value=0, max_value=100)
insulin = st.number_input("Insulin", min_value=0, max_value=900)
bmi = st.number_input("BMI", min_value=0.0, max_value=60.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5)
age = st.number_input("Age", min_value=0, max_value=120)

# Predict button
if st.button("Predict Diabetes"):
    input_data = np.array([[pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)[0][1]  # Probability of diabetes

    if prediction[0] == 1:
        st.error(f"⚠️ Patient is likely Diabetic (Probability: {proba:.2f})")
    else:
        st.success(f"✅ Patient is NOT Diabetic (Probability: {proba:.2f})")
