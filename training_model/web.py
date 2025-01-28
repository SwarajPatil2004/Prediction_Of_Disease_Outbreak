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
    
