import streamlit as st
from home import home  # import the home page function
from explanation import explanations  # import the explanations page function
# Import other pages similarly
# from calculations import calculations
# from lab import lab

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Explanation", "Calculation", "Lab"])

# Display the selected page
if page == "Home":
    home()
elif page == "Explanation":
    explanations()
elif page == "Calculation":
    calculations()  # Uncomment when you have this function ready
elif page == "Lab":
    lab()  # Uncomment when you have this function ready
