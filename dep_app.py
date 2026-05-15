import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_extras.let_it_rain import rain

model=pickle.load(open("house_model.pkl",'rb'))

st.title("The Prediction of price of the houses")
size=st.number_input("Enter the size")
bedrooms=st.slider("select range",1,6)

if st.button("Predict"):
    
    with st.spinner("Predicting..."):
        features=np.array([[size,bedrooms]])
        prediction=model.predict(features)[0]
    st.success(f"Predicted Price: ₹{prediction:,.2f}")
    st.balloons()
