import streamlit as st

# Import your page scripts
from pages import home, explanation, calculation, lab

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Home", "Explanation", "Calculation", "Lab"])

if page == "Home":
    home.show()  # Calls the show function in home.py

elif page == "Explanation":
    explanation.show()  # Calls the show function in explanation.py

elif page == "Calculation":
    calculation.show()  # Calls the show function in calculation.py

elif page == "Lab":
    lab.show()  # Calls the show function in lab.py
