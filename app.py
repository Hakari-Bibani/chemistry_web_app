import streamlit as st

# Load CSS for styling
def load_css():
    with open("styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Home Page
def home_page():
    st.title("Welcome to your virtual chemistry learning environment!")
    
    # Use a container for better styling
    with st.container():
        st.markdown("""
            📚 **What you can do here:**
            - Perform chemical calculations
            - Watch simulated reactions
            - Learn chemistry concepts
            
            🔬 **Getting Started:**
            1. Select a section on the left side
            2. Follow the instructions
            3. Experiment and learn!
        """)

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
