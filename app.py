import streamlit as st
from home import home
import streamlit as st
from explanation import show_explanation_section  # This should match your function name

def main():
    # Call the explanation section
    show_explanation_section()

if __name__ == "__main__":
    main()

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
