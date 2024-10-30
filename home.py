import streamlit as st

def home():
    # Set the page configuration first
    st.set_page_config(
        page_title="Chemistry Web App",
        page_icon="🧪",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Rest of the home page content
    st.title("🧪 Welcome to your Virtual Chemistry Lab 🧪")
    st.write("Explore and experiment with various chemistry concepts and reactions.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📚 What you can do here:")
        st.write("""
        - Perform chemical calculations
        - Watch simulated reactions
        - Learn chemistry concepts
        """)
    with col2:
        st.subheader("🔬 Getting Started:")
        st.write("""
        1. Select a section on the left side
        2. Follow the instructions
        3. Experiment and learn!
        """)

    # Add a chemistry-themed image
    st.image("images/chemistry_lab.png", use_column_width=True)
