import pickle
import streamlit as st
from streamlit_option_menu import option_menu
diab_model = pickle.load(open('diab_model.sav', 'rb'))
heart_final_model = pickle.load(open('heart_final_model.sav','rb'))
lung_model = pickle.load(open('lung_model.sav', 'rb'))
with st.sidebar:
    selected = option_menu('Concurrent Disease Prediction System',                       
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Lung Cancer Prediction'],
                          icons=['activity','heart-pulse','lungs'])    
#Diabetes Prediction Page
if (selected == 'Diabetes Disease Prediction'):
    st.title('DIABETES DISEASE PREDICTION')
    st.image('Screenshot (1).png')
    col1, col2= st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col1:
        Insulin = st.text_input('Insulin Level')
    
    with col2:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diab_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'SORRY!! YOU HAVE DIABETES'
        else:
          diab_diagnosis = "HURRAH!! YOU DON'T HAVE DIABETES "
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page tit
    st.title('HEART DISEASE PREDICTION')
    st.image('Screenshot (2).png')
    st.write("NOTE:")
    st.write("1. Gender : 0 = Female, 1 = Male")
    st.write("2. Chest Pain Types : 1 = typical angina, 2 = atypical angina, 3 = non — anginal pain, 4 = asymptotic")
    st.write("3. Fasting Blood Sugar : 1 = more than 120mg/dl, 0 = otherwise")
    st.write("4. Exercise induced angina : 1 = yes, 0 = no")
    st.write("5. Number of major vessels : (0–3) colored by flourosopy")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Gender')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure in mg/dl')
        
    with col2:
        chol = st.text_input('Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
        
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
        heart_prediction = heart_final_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'SORRY!! YOU HAVE HEART DISEASE'
        else:
          heart_diagnosis = "HURRAH!! YOU DON'T HAVE HEART DISEASE"
        
    st.success(heart_diagnosis)

if(selected == "Lung Cancer Prediction"):
    #page title
    st.title("LUNG CANCER PREDICTION")
    st.image('lung img.jpg')
    st.write("NOTE:")
    st.write("1. Gender : 0 = Female, 1 = Male")
    st.write("1. If you have symptoms/habit = 2; else = 1")
# getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        GENDER = st.number_input("GENDER")
        
    with col2:
        AGE = st.number_input("AGE")
    
    with col3:
        SMOKING = st.number_input("SMOKING")
    
    with col1:
        YELLOW_FINGERS = st.number_input("YELLOW_FINGERS")
    
    with col2:
        ANXIETY = st.number_input("ANXIETY")
    
    with col3:
        PEER_PRESSURE = st.number_input("PEER_PRESSURE")
    
    with col1:
        CHRONIC_DISEASE = st.number_input("CHRONIC DISEASE")
    
    with col2:
        FATIGUE = st.number_input("FATIGUE")
    
    with col3:
        ALLERGY = st.number_input("ALLERGY")
    
    with col1:
        WHEEZING = st.number_input("WHEEZING")
    
    with col2:
        ALCOHOL_CONSUMING = st.number_input("ALCOHOL CONSUMING")
    
    with col3:
        COUGHING = st.number_input("COUGHING")
    
    with col1:
        SHORTNESS_OF_BREATH = st.number_input("SHORTNESS OF BREATH")
    
    with col2:
        SWALLOWING_DIFFICULTY = st.number_input("SWALLOWING DIFFICULTY")
    
    with col3:
        CHEST_PAIN = st.number_input("CHEST PAIN")
    


# code for Prediction
    lung_cancer_result = " "
    
    # creating a button for Prediction
    
    if st.button("Lung Cancer Test Result"):
        lung_cancer_report = lung_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        
        if (lung_cancer_report[0] == 0):
          lung_cancer_result = "HURRAH!! YOU DON'T HAVE LUNG CANCER"
        else:
          lung_cancer_result = "SORRY!! YOU HAVE LUNG CANCER"
        
    st.success(lung_cancer_result)
 