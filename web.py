import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title= "Prediction of Disease Outbreak",
                   layout="wide",
                   page_icon=":doctor:")
diabetes_model= pickle.load(open(r"C:\Users\Sheetal Patil\Documents\GitHub\Prediction_Of_Disease_Outbreak\training_model\daibetes\diabetes_model.sav", "rb"))
heart_disease= pickle.load(open(r"C:\Users\Sheetal Patil\Documents\GitHub\Prediction_Of_Disease_Outbreak\training_model\heart\heart_disease_model.sav", "rb"))
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
        Bloodpressure= st.text_input('Blood Pressure')
    with col1:
        Skinthickness= st.text_input('Skin thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI= st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function')
    with col2:
        Age= st.text_input("Age")

diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    user_input = [Pregnancies, Glucose, Bloodpressure, Skinthickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    user_input = [float(x) for x in user_input]
    diab_prediction = diabetes_model.predict([user_input])
    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'
st.success(diab_diagnosis)
