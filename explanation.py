import streamlit as st

def show_explanations():
    st.title("📚 Chemistry Concepts & Explanation")
    
    # Load the CSS file
    st.markdown(
        '<link href="styles_explanation.css" rel="stylesheet" type="text/css">',
        unsafe_allow_html=True
    )
    
    # Glowing title
    st.markdown('<h1 class="glowing-title">📚 Chemistry Concepts & Explanation</h1>', unsafe_allow_html=True)

    # Options
    st.subheader("Select a topic to learn about:")
    topics = ["pH", "pOH", "Molarity"]
    selected_topic = st.selectbox("Choose a topic:", topics)

    # Cards for each option
    st.markdown('<div class="topic-cards">', unsafe_allow_html=True)
    for topic in topics:
        st.markdown(f'''
            <div class="card" onclick="document.getElementById('{topic}').style.display='block'">
                <h3>{topic}</h3>
                <p>Click to learn more about {topic}</p>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Display the selected topic
    if selected_topic == "pH":
        st.subheader("Understanding pH")
        st.write("What is pH?")
        st.write("pH is a measure of the hydrogen ion concentration in a solution...")
        st.write("Common Examples:\n• Lemon juice: pH 2 (acidic) ...")
        st.write("### Test Your Knowledge! 📝")
        pH_question = st.selectbox("What pH value represents a neutral solution?", ["0", "7", "14", "3.5"])
        if pH_question:
            st.markdown('<div class="test-knowledge">', unsafe_allow_html=True)
            if pH_question == "7":
                st.markdown("<p class='correct-answer'>Correct! The pH value representing a neutral solution is 7.</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p class='correct-answer'>Incorrect. The correct answer is 7.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    elif selected_topic == "pOH":
        st.subheader("Understanding pOH")
        st.write("What is pOH?")
        st.write("pOH is a measure of the hydroxide ion concentration in a solution...")
        st.write("### Test Your Knowledge! 📝")
        pOH_question = st.selectbox("What pOH value represents a neutral solution?", ["0", "7", "14", "3.5"])
        if pOH_question:
            st.markdown('<div class="test-knowledge">', unsafe_allow_html=True)
            if pOH_question == "7":
                st.markdown("<p class='correct-answer'>Correct! The pOH value representing a neutral solution is 7.</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p class='correct-answer'>Incorrect. The correct answer is 7.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    elif selected_topic == "Molarity":
        st.subheader("Understanding Molarity")
        st.write("What is Molarity?")
        st.write("Molarity (M) is a measure of the concentration of a solution...")
        st.write("### Test Your Knowledge! 📝")
        molarity_question = st.selectbox("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?", ["0.5 M", "1.0 M", "2.0 M", "4.0 M"])
        if molarity_question:
            st.markdown('<div class="test-knowledge">', unsafe_allow_html=True)
            if molarity_question == "4.0 M":
                st.markdown("<p class='correct-answer'>Correct! The molarity is 4.0 M.</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p class='correct-answer'>Incorrect. The correct answer is 4.0 M.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Call the function to display the explanations
if __name__ == "__main__":
    show_explanations()
