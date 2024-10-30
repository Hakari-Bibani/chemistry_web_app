import streamlit as st

def home():
    st.title("Welcome to your virtual chemistry learning environment!")
    
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
