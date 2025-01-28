import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title= "Prediction of Disease Outbreak",
                   layout="wide",
                   page_icon=":doctor:")
diabetes_model= pickle.load(open(r"C:\Users\Sheetal Patil\Documents\GitHub\Prediction_Of_Disease_Outbreak\training_model\daibetes\diabetes_model.sav", "rb"))
heart_disease_model= pickle.load(open(r"C:\Users\Sheetal Patil\Documents\GitHub\Prediction_Of_Disease_Outbreak\training_model\heart\heart_disease_model.sav", "rb"))
parkinsons= pickle.load(open(r"C:\Users\Sheetal Patil\Documents\GitHub\Prediction_Of_Disease_Outbreak\training_model\parkinsons\parkinsons_prediction_model", "rb"))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak sustem',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                          menu_icon="hospital-fill", icons=['activity','heart','person'],
                          default_index=0)
    
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3= st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3: 
        BloodPressure= st.text_input('Blood Pressure')
    with col1:
        SkinThickness= st.text_input('Skin thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI= st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function')
    with col2:
        Age= st.text_input("Age")
    diab_diagnosis = 'Enter the details above'
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        if '' in user_input:
            diab_diagnosis= "Please fill the necessary details"
        else:
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)


elif selected== 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3= st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Gender')
    with col3:
        cp = st.text_input('Chest Pain Type (cp)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (trestbps)')
    with col2:
        chol = st.text_input('Serum Cholestoral (chol)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (fbs)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (restecg)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
    with col3:
        exang = st.text_input('Exercise Induced Angina (exang)')
    with col1:
        oldpeak = st.text_input('ST depression (oldpeak)')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (slope)')
    with col3:
        ca = st.text_input('Number of Major Vessels (ca)')
    with col1:
        thal = st.text_input('Thalassemia (thal)')

    heart_disease_diagnosis = 'Enter the details above'
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        if '' in user_input:
            heart_disease_diagnosis= "Please fill all the above details."
        else:
            user_input = [float(x) for x in user_input]
            heart_disease_prediction = heart_disease_model.predict([user_input])
            if heart_disease_prediction[0] == 1:
                heart_disease_diagnosis = 'The person has heart disease'
            else:
                heart_disease_diagnosis = 'The person does not have heart disease'
            
    st.success(heart_disease_diagnosis)
