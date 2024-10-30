import streamlit as st
from home import home
from explanation import explanation
def explanation_page():
    # Glowing title for explanation section
    st.markdown('<h1 class="glowing-title-explanation">📚 Chemistry Concepts & Explanation</h1>', unsafe_allow_html=True)

    # Create styled cards for pH, pOH, Molarity
    st.markdown('<div class="explanation-cards">', unsafe_allow_html=True)
    
    topics = {
        "pH": "Understanding pH<br>What is pH? pH is a measure of the hydrogen ion concentration in a solution.",
        "pOH": "Understanding pOH<br>What is pOH? pOH is a measure of the hydroxide ion concentration in a solution.",
        "Molarity": "Understanding Molarity<br>What is Molarity? Molarity is a measure of the concentration of a solution."
    }
    
    for topic, description in topics.items():
        st.markdown(f'''
            <div class="card" onclick="document.getElementById('{topic}').style.display='block'">
                <h2>{topic}</h2>
                <p>{description}</p>
            </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Test Your Knowledge Section
    for topic in topics.keys():
        st.markdown(f'<div id="{topic}" style="display:none;">', unsafe_allow_html=True)
        st.markdown('<div class="test-your-knowledge">', unsafe_allow_html=True)
        st.markdown(f"**Test Your Knowledge!** 📝 What is the correct answer for {topic}?")
        if topic == "pH":
            options = ["0", "7", "14", "3.5"]
            answer = "7"
        elif topic == "pOH":
            options = ["0", "7", "14", "3.5"]
            answer = "7"
        elif topic == "Molarity":
            options = ["0.5 M", "1.0 M", "2.0 M", "4.0 M"]
            answer = "4"

        user_answer = st.selectbox("Select your answer:", options)
        if st.button("Submit"):
            if user_answer == answer:
                st.success("Correct! 🎉")
            else:
                st.error(f"Incorrect! The correct answer is {answer}.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
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
