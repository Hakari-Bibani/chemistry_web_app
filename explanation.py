import streamlit as st

def explanation():
    # Hero Section
    st.markdown('<h1 class="glowing-title">📚 Chemistry Concepts & Explanation</h1>', unsafe_allow_html=True)
    
    # Topics Section
    st.write("### Select a topic to learn about:")
    st.markdown(
        """
        <div class="option-cards">
            <div class="option-card" onclick="show_topic('pH')">pH</div>
            <div class="option-card" onclick="show_topic('pOH')">pOH</div>
            <div class="option-card" onclick="show_topic('Molarity')">Molarity</div>
        </div>
        """, unsafe_allow_html=True
    )

    # Functions for each topic
    def show_topic(topic):
        if topic == "pH":
            show_ph_topic()
        elif topic == "pOH":
            show_poh_topic()
        elif topic == "Molarity":
            show_molarity_topic()

    # Content for each topic
    def show_ph_topic():
        st.write("### Understanding pH")
        st.write("pH is a measure of the hydrogen ion concentration...")
        # Knowledge Check
        st.write("#### Test Your Knowledge! 📝")
        if st.button("What pH value represents a neutral solution?"):
            options = [("0", False), ("7", True), ("14", False), ("3.5", False)]
            show_quiz(options)

    def show_poh_topic():
        st.write("### Understanding pOH")
        st.write("pOH is a measure of the hydroxide ion concentration...")
        # Knowledge Check
        st.write("#### Test Your Knowledge! 📝")
        if st.button("What pOH value represents a neutral solution?"):
            options = [("0", False), ("7", True), ("14", False), ("3.5", False)]
            show_quiz(options)

    def show_molarity_topic():
        st.write("### Understanding Molarity")
        st.write("Molarity is a measure of the concentration of a solution...")
        # Knowledge Check
        st.write("#### Test Your Knowledge! 📝")
        if st.button("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?"):
            options = [("0.5 M", False), ("1.0 M", False), ("2.0 M", False), ("4.0 M", True)]
            show_quiz(options)

    # Quiz Functionality
    def show_quiz(options):
        for option, is_correct in options:
            if st.button(option):
                if is_correct:
                    st.success("Correct!")
                else:
                    st.error("That's not correct.")

    # JavaScript for showing topics on click (optional)
    st.markdown("""
    <script>
    function show_topic(topic) {
        Streamlit.setComponentValue(topic);
    }
    </script>
    """, unsafe_allow_html=True)

# Run the explanation function to display content
explanation()
