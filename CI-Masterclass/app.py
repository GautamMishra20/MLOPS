import streamlit as st

# streamlit ui
st.title("power claculator")
st.write("Enter a number to calculator its sq., cube, and fifth power.")

# Get user input
n = st.number_input("Enter an integer", value=1, step=1)

# calculate results
sq = n ** 2
cube = n ** 3 
fifth_power = n ** 5

# Display results
st.write(f"The Sq. of {n} is: {sq}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")