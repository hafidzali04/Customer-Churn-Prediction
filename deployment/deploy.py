# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 18:51:25 2022

@author: Ali
"""

import streamlit as st
import pandas as pd
from tensorflow import keras
from PIL import Image

st.header('CUSTOMER CHURN PREDICTION')
st.caption(""" 
         * The features like SeniorCitizen,Partner,Dependents,PaperlessBilling is 0 : no and 1 : yes             
         
         * features for services coloum is is 0 : no , 1 : no internet service and 2 : yes
         
         * features for Contract coloum  is is 0 : Month-to-month  , 1 : Two year and 2 : One year 
         
         * features for Payment Method coloum  is is 0 : Electronic check  , 1 : Mailed check  , 
                                                     2 : Bank transfer (automatic), 3 : Credit card (automatic)     
         Use the sidebar to select input features.
         """)
image = Image.open('churnim.png')

st.image(image)
@st.cache
def fetch_data():
    df = pd.read_csv('https://raw.githubusercontent.com/hafidzali04/Hacktiv8-phase0/main/data/dfclean.csv')
    return df

df = fetch_data()
#st.write(df)

st.sidebar.header('User Input Features')

def user_input():
    SeniorCitizen = st.sidebar.selectbox('Senior Citizen', df['SeniorCitizen'].unique())
    Partner = st.sidebar.selectbox('Partner', df['Partner'].unique())
    Dependents = st.sidebar.selectbox('Dependents ', df['Dependents'].unique())
    tenure = st.sidebar.number_input('Tenure', 0.0, value=5.0)
    st.sidebar.write('--------------')
    st.sidebar.subheader('Services')
    OnlineSecurity = st.sidebar.selectbox('OnlineSecurity ', df['OnlineSecurity'].unique())
    OnlineBackup = st.sidebar.selectbox('OnlineBackup ', df['OnlineBackup'].unique())
    DeviceProtection = st.sidebar.selectbox('DeviceProtection ', df['DeviceProtection'].unique())
    TechSupport = st.sidebar.selectbox('TechSupport ', df['TechSupport'].unique())
    st.sidebar.write('--------------')
    Contract = st.sidebar.selectbox('Contract', df['Contract'].unique())
    PaperlessBilling = st.sidebar.selectbox('PaperlessBilling', df['PaperlessBilling'].unique())
    PaymentMethod = st.sidebar.selectbox('PaymentMethod', df['PaymentMethod'].unique())
    MonthlyCharges = st.sidebar.number_input('MonthlyCharges', 0.0, value=54.55)
    TotalCharges = st.sidebar.number_input('TotalCharges', 0.0, value=385.55)
   
						
    data = {
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'Contract': Contract,
        'PaperlessBilling':PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }
    features = pd.DataFrame(data, index=[0])
    return features


input = user_input()


#st.subheader('User Input')
#st.write(input)
if st.button('Predict'):
    model = keras.models.load_model("Churn_model")
    prediction = model.predict(input)
    st.write('Based on user input, predicted is: ')
    st.write(prediction[0][0])
    if(prediction>0.5):
      prediction='Customer churn'
      st.error(prediction)
    else :
      prediction='Customer not churn'
      st.success(prediction)
else:
     st.write('Goodbye')
     

#st.write(prediction)
