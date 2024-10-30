import streamlit as st

# Link the CSS file
def load_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS
load_css()

# Your home page content
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
