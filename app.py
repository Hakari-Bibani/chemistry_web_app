import streamlit as st

# Custom CSS to style the app
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff; /* Light blue background */
        background-image: url('images/chemistry_lab.png'); /* Correct path to your background image */
        background-size: cover; /* Ensure the image covers the entire viewport */
        background-repeat: no-repeat; /* Prevent the image from repeating */
        background-attachment: fixed; /* Keep the background fixed during scroll */
        font-family: 'Arial', sans-serif; /* Font style */
        color: #333; /* Text color */
    }

    .container {
        padding: 20px; /* Padding for content area */
        border-radius: 10px; /* Rounded corners */
        background-color: rgba(255, 255, 255, 0.8); /* White background with transparency */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow for depth */
    }
    </style>
    """,
    unsafe_allow_html=True
)


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
