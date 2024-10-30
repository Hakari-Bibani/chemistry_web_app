import streamlit as st
from home import home  # import the home page function

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Explanation", "Calculation", "Lab"])

# Display the selected page
if page == "Home":
    home()
# Add elif blocks for the other pages when they're ready
