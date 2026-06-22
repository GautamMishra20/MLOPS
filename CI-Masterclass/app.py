import streamlit as st

# streamlit ui
st.title("power claculator")
st.write("Enter a number to calculator its sq., cube, and fifth power.")

# Get user input
n = st.number_input("Enter an integer", value=1, step=1)

# calculate results
# sq = n ** 2
# cube = n ** 3 
# fifth_power = n ** 5

def sq(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

# Display results
st.write(f"The Sq. of {n} is: {sq(n)}")
st.write(f"The cube of {n} is: {cube(n)}")
st.write(f"The fifth power of {n} is: {fifth_power(n)}")