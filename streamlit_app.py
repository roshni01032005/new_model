
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('best_salary_prediction_model.pkl')

st.title('Salary Prediction App')
st.write('Enter the details below to predict the salary.')

# Input fields for features (using numerical inputs for encoded categorical features)
education = st.selectbox('Education (0=Bachelor, 1=High School, 2=Master, 3=PhD)', options=[0, 1, 2, 3]) # Assuming these are the encoded values
experience = st.slider('Experience (Years)', min_value=0, max_value=50, value=10)
location = st.selectbox('Location (0=Rural, 1=Suburban, 2=Urban)', options=[0, 1, 2]) # Assuming these are the encoded values
job_title = st.selectbox('Job Title (0=Analyst, 1=Director, 2=Engineer, 3=Manager, 4=Sales)', options=[0, 1, 2, 3, 4]) # Assuming these are the encoded values
age = st.slider('Age', min_value=18, max_value=70, value=30)
gender = st.selectbox('Gender (0=Female, 1=Male)', options=[0, 1]) # Assuming these are the encoded values

if st.button('Predict Salary'):
    # Create a DataFrame from the input values
    input_data = pd.DataFrame([{
        'Education': education,
        'Experience': experience,
        'Location': location,
        'Job_Title': job_title,
        'Age': age,
        'Gender': gender
    }])

    # Make prediction
    predicted_salary = model.predict(input_data)[0]

    st.success(f'Predicted Salary: ${predicted_salary:,.2f}')
