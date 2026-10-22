import streamlit as st

st.title("Marvellous Infosystems")

st.header("Simple Interest Calculator")

Principal_Amount = st.number_input("Enter the Principal Amount")
Rate_Of_Interest = st.number_input("Enter the Rate Of Interest")
Time_Period = st.number_input("Enter the Time Period")

st.button("Calculate")

Simple_Interest = (Principal_Amount * Rate_Of_Interest * Time_Period)

st.success("The Simple Interest is : "+str(Simple_Interest))