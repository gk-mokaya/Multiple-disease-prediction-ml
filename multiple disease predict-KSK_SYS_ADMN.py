# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 07:50:17 2024

@author: mcpyk
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("C:/Users/kevin/OneDrive/Documents/Multiple Diease Prediction System/Models/diabetes_model.sav", 'rb'))

breast_disease_model = pickle.load(open("C:/Users/kevin/OneDrive/Documents/Multiple Diease Prediction System/Models/breast_cancer_model.sav", 'rb'))

heart_disease_model = pickle.load(open("C:/Users/kevin/OneDrive/Documents/Multiple Diease Prediction System/Models/heart_disease_model.sav", 'rb'))

parkinsons_model = pickle.load(open("C:/Users/kevin/OneDrive/Documents/Multiple Diease Prediction System/Models/parkinsons_model.sav", 'rb'))


# sidebar navi bar

with st.sidebar:
    selected = option_menu("Disease Menu",
                           
                           ["Diabetes Diseases",
                            "Breast Diseases",
                            "Heart Diseases",
                            "Parkinsons Diseases"],
                           
                           icons= ['bandaid','person-standing-dress','postcard-heart','headset-vr'],
                           default_index = 0)

# Diabetses prediction page
if (selected == "Diabetes Diseases"):
    #page title
    st.title("DIABETES DISEASE PREDICTION")
    
    # Getting the input data from the user
    # Columns for input fileds
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    # code for prediction
    diabetes_prediction = ''
    
    #creating button for prediction
    if st.button('Diagnose'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(diabetes_prediction[0]==1):
            diabetes_prediction = 'DIABETIC'
            # Initialize session state to track the current page
        if 'page' not in st.session_state:
            st.session_state.page = 'home'
        # Define a function to switch pages
        def go_to_page(page_name):
            st.session_state.page = page_name
        # Home Page
        if st.session_state.page == 'home':
            st.title("Recommendation")
            st.write("Welcome to the Home Page!")
            # Button to navigate to the About page
            if st.button("Go to About Page"):
                go_to_page('about')
        # About Page
        elif st.session_state.page == 'about':
            st.title("About Page")
            st.write("This is the About Page.")
        else:
            diabetes_prediction = "NOT DIABETIC"
            
    st.success(diabetes_prediction) 
    
    
    
    


    
    
    
    
    
# Breast prediction page    
if (selected == "Breast Diseases"):
    
    #page title
    st.title("BREAST DISEASE PREDICTION")
    
    # Getting the input data from the user
    # Columns for input fileds
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        meanradius = st.text_input('Mean radius of tumor')
    with col2:
        meantexture = st.text_input('Mean texture of tumor')
    with col3:
        meanperimeter = st.text_input('Mean perimeter of tumor')
    with col1:
        meanarea  = st.text_input('Mean area of tumor')
    with col2:
        meansmoothness = st.text_input('Mean smoothness of tumor')
    with col3:
        meancompactness = st.text_input('Mean compactness of tumor')
    with col1:
        meanconcavity = st.text_input('Mean concavity of tumor')
    with col2:
        meanconcavepoints = st.text_input('Mean number of concave portions')
    with col3:
        meansymmetry = st.text_input('symmetry_mean')
    with col1:
        meanfractaldimension = st.text_input('fractal_dimension_mean')
    with col2:
        radiuserror = st.text_input('Radius error')
    with col3:
        textureerror = st.text_input('Text error')
    with col1:
        perimetererror  = st.text_input('Perimeter Error')
    with col2:
        areaerror = st.text_input('Area Error')
    with col3:
        smoothnesserror = st.text_input('Smoothnness error')
    with col1:
        compactnesserror = st.text_input('Compactness error')
    with col2:
        concavityerror = st.text_input('Concavity error')
    with col3:
        concavepointserror = st.text_input('Concave point error')     
    with col1:
        symmetryerror = st.text_input('Symmetry error')
    with col2:
        fractaldimensionerror = st.text_input('Fractional Dimension error')
    with col3:
        worstradius = st.text_input('Worst Radius')
    with col1:
        worsttexture  = st.text_input('Worst Texture')
    with col2:
        worstperimeter = st.text_input('Worst Perimeter')
    with col3:
        worstarea = st.text_input('Worst Area')
    with col1:
        worstsmoothness = st.text_input('Worst Smoothness')
    with col2:
        worstcompactness = st.text_input('Worst commpactness')
    with col3:
        worstconcavity = st.text_input('Worst concavity')
    with col1:
        worstconcavepoints = st.text_input('Worst concave points')
    with col2:
        worstsymmetry = st.text_input('Worst symmetry')
    with col3:
        worstfractaldimension = st.text_input('Worst fractional dimension')


    # code for prediction
    breast_cancer_prediction = ''
    
    #creating button for prediction
    if st.button('Diagnose'):
        
        user_input = [meanradius, meantexture, meanperimeter, meanarea, meansmoothness, meancompactness, meanconcavity, meanconcavepoints, meansymmetry, meanfractaldimension, radiuserror, textureerror, perimetererror, areaerror, smoothnesserror, compactnesserror, concavityerror, concavepointserror, symmetryerror, fractaldimensionerror, worstradius, worsttexture, worstperimeter, worstarea, worstsmoothness, worstcompactness, worstconcavity, worstconcavepoints, worstsymmetry, worstfractaldimension]

        user_input = [float(x) for x in user_input]

        breast_cancer_prediction = breast_disease_model.predict([user_input])
        
        if(breast_cancer_prediction[0]==1):
            breast_cancer_prediction = 'SUFFERING FROM BEGNIN'
        else:
            breast_cancer_prediction = "SUFFERING FROM MALIGNANT"
            
    st.success(breast_cancer_prediction)
    
  
# Heart prediction page    
if (selected == "Heart Diseases"):
    
    #page title
    st.title("HEART DISEASE PREDICTION")
    
    # Getting the input data from the user
    # Columns for input fileds
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Diseases":

    # page title
    st.title("Parkinsons Disease")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('Average vocal fundamental frequency(Hz)')

    with col2:
        fhi = st.text_input('Maximum vocal fundamental frequency(Hz)')

    with col3:
        flo = st.text_input('Minimun vocal fundamental frequency(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)