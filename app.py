import streamlit as st
from home import home
from explanation import explanation_page  # Import updated function name
from calculations import calculations
from lab import lab

# Function to load pages
pages = {
    "Home": home,
    "Explanations": explanation_page,
    "Calculations": calculations,
    "Lab": lab
}

selection = st.sidebar.selectbox("Go to", list(pages.keys()))
pages[selection]()

from home import home
from explanation import explanation
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

