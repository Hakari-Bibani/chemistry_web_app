import streamlit as st
# Load CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

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
