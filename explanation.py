import streamlit as st

def explanation_page():
    # Glowing Title
    st.markdown('<h1 class="glowing-title">📚 Chemistry Concepts & Explanations</h1>', unsafe_allow_html=True)

    # Cards for options (pH, pOH, Molarity)
    options = ["pH", "pOH", "Molarity"]
    selected_option = st.selectbox("Select a topic to learn about:", options)

    if selected_option == "pH":
        st.write("Understanding pH")
        st.write("""
            **What is pH?**
            pH is a measure of the hydrogen ion concentration in a solution...
        """)
        # Test Your Knowledge!
        st.write("Test Your Knowledge! 📝")
        pH_question = st.selectbox("What pH value represents a neutral solution?", [0, 7, 14, 3.5])
        if st.button("Submit"):
            if pH_question == 7:
                st.success("Correct! The pH value representing a neutral solution is 7.")
            else:
                st.error("Incorrect. The correct answer is 7.")

    elif selected_option == "pOH":
        st.write("Understanding pOH")
        st.write("""
            **What is pOH?**
            pOH is a measure of the hydroxide ion concentration in a solution...
        """)
        # Test Your Knowledge!
        st.write("Test Your Knowledge! 📝")
        pOH_question = st.selectbox("What pOH value represents a neutral solution?", [0, 7, 14, 3.5])
        if st.button("Submit"):
            if pOH_question == 7:
                st.success("Correct! The pOH value representing a neutral solution is 7.")
            else:
                st.error("Incorrect. The correct answer is 7.")

    elif selected_option == "Molarity":
        st.write("Understanding Molarity")
        st.write("""
            **What is Molarity?**
            Molarity (M) is a measure of the concentration of a solution...
        """)
        # Test Your Knowledge!
        st.write("Test Your Knowledge! 📝")
        molarity_question = st.selectbox("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?", [0.5, 1.0, 2.0, 4.0])
        if st.button("Submit"):
            if molarity_question == 4:
                st.success("Correct! The molarity is 4 M.")
            else:
                st.error("Incorrect. The correct answer is 4 M.")
