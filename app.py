import streamlit as st
import pickle
import numpy as np

st.title("Check the environment")

carbon_emmission=st.number_input("Carbon emission Amount:",min_value=0.0,format="%f")
energy_output=st.number_input("Energy Output Value:",min_value=0.0,format="%f")
renewability_index=st.number_input("renewability_index:",min_value=0.0,format="%f")
cost_efficiency=st.number_input("Cost Efficiency:",min_value=0.0,format="%f")


with open('lrmodel_sustainable.pkl','rb')as file:
    model=pickle.load(file)

if st.button("Predict"):
    input_data=np.array([[carbon_emmission,energy_output,renewability_index,cost_efficiency]])

    prediction=model.predict(input_data)

    if prediction[0]== 1:
        st.success("Congrats, this environment is sustainable")
    else:
        st.info("This environment is not sustainable")


