import streamlit as st
from explanation import explanation_page

def main():
    st.title("Virtual Chemistry Learning Environment")
    menu = ["Home", "Explanation", "Calculation", "Lab"]
    choice = st.sidebar.selectbox("Select a section", menu)

    if choice == "Home":
        st.write("Welcome to your virtual chemistry learning environment!")
        st.write("📚 What you can do here:")
        st.write("• Perform chemical calculations")
        st.write("• Watch simulated reactions")
        st.write("• Learn chemistry concepts")
        st.write("🔬 Getting Started:")
        st.write("1. Select a section on the left side")
        st.write("2. Follow the instructions")
        st.write("3. Experiment and learn!")

    elif choice == "Explanation":
        explanation_page()

    elif choice == "Calculation":
        st.write("Welcome to the Calculation section! Select calculation type: pH, molarity")

    elif choice == "Lab":
        st.write("Welcome to the virtual lab! Here you can simulate different chemical reactions.")

if __name__ == "__main__":
    main()
