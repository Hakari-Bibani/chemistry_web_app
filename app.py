import streamlit as st
from home import home
from explanation import explanation_page  # Change made here
from calculations import calculations
from lab import lab

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Explanation", "Calculations", "Lab"])

# Display the selected page
if page == "Home":
    home()
elif page == "Explanation":
    explanation()
elif page == "Calculations":
    calculations()
elif page == "Lab":
    lab()
