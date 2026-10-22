import streamlit as st

st.title("Marvellous Infosystems")

st.header("Student Result Calculator")

Student_Name = st.text_input("Enter Student Name")

Subject1 = st.number_input("Enter the 1st Subject Marks")
Subject2 = st.number_input("Enter the 2nd Subject Marks")
Subject3 = st.number_input("Enter the 3rd Subject Marks")

if st.button("Calculate_Result"):

    Total_Marks = Subject1+Subject2+Subject3
    Percentage = (Total_Marks/300) * 100

    st.write("Student Name : ",Student_Name)
    st.write("Total Marks : ",Total_Marks)
    st.write("Percentage : ",str(round(Percentage,2))+"%")

    if Subject1 >= 40 and Subject2 >= 40 and Subject3 >= 40:
        st.success("Student is Passed")
    else:
        st.error("Student is Failed")
    

