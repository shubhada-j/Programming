import streamlit as st

st.title("Marvellous Infosystems")

st.header("Even or Odd Number")

no = st.number_input("Enter the number : ",value=0,step=1)

st.button("Check_Number")

if no % 2 == 0 : 
    st.success("Even Number")
else:
    st.success("Odd Number")