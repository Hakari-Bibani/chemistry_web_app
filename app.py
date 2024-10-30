import streamlit as st
from home import home  # import the home page function
from explanation import explanation  # import the explanation page function
from calculation import calculation  # import the calculation page function
from lab import lab  # import the lab page function

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Explanation", "Calculation", "Lab"])

# Display the selected page
if page == "Home":
    home()
elif page == "Explanation":
    explanation()  # call the explanation page function
elif page == "Calculation":
    calculation()  # call the calculation page function
elif page == "Lab":
    lab()  # call the lab page function
