import streamlit as st

# Add the CSS for styling
st.markdown(
    """
    <style>
    body {
        background-image: url('chemistry_lab.png'); /* Ensure this path is correct */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white; /* Change text color for better visibility */
        font-family: Arial, sans-serif; /* Font style for the text */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your existing code for the home page...
st.title("Welcome to your virtual chemistry learning environment!")
st.subheader("📚 What you can do here:")
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
