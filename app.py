import streamlit as st

# Load CSS
def load_css():
    with open("styles.css") as f:  # Ensure the correct file name is used
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS
load_css()

# Home page function
def home_page():
    st.title("Welcome to your virtual chemistry learning environment!")
    st.write("📚 What you can do here:")
    st.write("• Perform chemical calculations")
    st.write("• Watch simulated reactions")
    st.write("• Learn chemistry concepts")
    st.write("🔬 Getting Started:")
    st.write("1. Select a section on the left side")
    st.write("2. Follow the instructions")
    st.write("3. Experiment and learn!")

# Call the home page function
home_page()
