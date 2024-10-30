import streamlit as st
from home import home
from explanation import explanations
from calculations import calculations  # Make sure this is imported
from lab import lab  # Make sure this is imported

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Explanation", "Calculation", "Lab"])

# Display the selected page
if page == "Home":
    home()
elif page == "Explanation":
    explanations()
elif page == "Calculation":  # Note: matches exactly with the radio button option
    calculations()
elif page == "Lab":
    lab()
