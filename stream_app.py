import streamlit as st

# Slider to select age
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# App title
st.title('My First Streamlit App')

# Welcome message
st.write('Welcome to this simple Streamlit application.')

# Button to say hello, and conditional response
if st.button('Say hello'):
    st.write('Hello there!')
else:
    st.write('Goodbye!')


