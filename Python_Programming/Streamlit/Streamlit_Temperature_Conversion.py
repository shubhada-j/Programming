import streamlit as st

st.title("Marvellous Infosystems")

st.header("Celsius to Fahrenheit Convertor")

Celsius_Temprtaure = st.number_input("Enter the temperature in celsius")

if st.button("Convert"):
    Fahrenheit_Temprtaure = (Celsius_Temprtaure * 1.8) + 32 

    st.success("Temperature in Fahrenheit : "+str(Fahrenheit_Temprtaure))