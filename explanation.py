import streamlit as st

# Apply custom CSS for neon effect and card layout
st.markdown("""
    <style>
    /* Glowing Title */
    .glowing-title {
        font-size: 2.5em;
        text-align: center;
        color: black;
        text-shadow: 0 0 10px #00e6e6, 0 0 20px #00e6e6, 0 0 30px #00e6e6, 0 0 40px #00e6e6;
        animation: text-glow 1.5s infinite alternate;
    }

    @keyframes text-glow {
        from { text-shadow: 0 0 5px #00e6e6, 0 0 10px #00e6e6; }
        to { text-shadow: 0 0 20px #00e6e6, 0 0 30px #00e6e6; }
    }

    /* Topic Cards */
    .topic-cards {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
    }
    .card {
        background: #e3f2fd;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        width: 30%;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
        cursor: pointer;
        transition: transform 0.3s;
    }
    .card:hover {
        transform: translateY(-10px);
        background: #b3e5fc;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="glowing-title">📚 Chemistry Concepts & Explanation</div>', unsafe_allow_html=True)

st.write("Welcome to the explanations section! Here you'll find detailed information about various chemistry concepts.")

# Topic selection cards
selected_topic = st.radio("Select a topic to learn about:", ("pH", "pOH", "Molarity"))

# Show explanations based on selected topic
if selected_topic == "pH":
    st.subheader("Understanding pH")
    st.write("""
    **What is pH?**  
    pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.
    **The pH Scale:**
    - pH < 7: Acidic
    - pH = 7: Neutral
    - pH > 7: Basic (Alkaline)

    **Calculating pH:**  
    pH = -log[H⁺], where [H⁺] is the concentration of hydrogen ions in mol/L.

    **Common Examples:**
    - Lemon juice: pH 2 (acidic)
    - Pure water: pH 7 (neutral)
    - Baking soda: pH 9 (basic)
    """)

    # Quiz for pH
    st.subheader("Test Your Knowledge! 📝")
    question = st.radio("What pH value represents a neutral solution?", ["0", "7", "14", "3.5"])
    if st.button("Submit Answer"):
        st.write("The correct answer is: 7")

elif selected_topic == "pOH":
    st.subheader("Understanding pOH")
    st.write("""
    **What is pOH?**  
    pOH is a measure of the hydroxide ion concentration in a solution. It's a scale similar to pH that indicates how acidic or basic a solution is.

    **The pOH Scale:**
    - pOH < 7: Basic (Alkaline)
    - pOH = 7: Neutral
    - pOH > 7: Acidic

    **Calculating pOH:**  
    pOH = -log[OH⁻], where [OH⁻] is the concentration of hydroxide ions in mol/L.

    **Relationship between pH and pOH:**  
    In any aqueous solution at 25°C, pH + pOH = 14.

    **Common Examples:**
    - Strong base (sodium hydroxide): pOH < 7 (basic)
    - Pure water: pOH = 7 (neutral)
    - Strong acid (hydrochloric acid): pOH > 7 (acidic)
    """)

    # Quiz for pOH
    st.subheader("Test Your Knowledge! 📝")
    question = st.radio("What pOH value represents a neutral solution?", ["0", "7", "14", "3.5"])
    if st.button("Submit Answer"):
        st.write("The correct answer is: 7")

elif selected_topic == "Molarity":
    st.subheader("Understanding Molarity")
    st.write("""
    **What is Molarity?**  
    Molarity (M) is a measure of the concentration of a solution, expressed as the number of moles of solute per liter of solution.

    **Calculating Molarity:**  
    M = moles of solute / liters of solution

    **Important Concepts:**
    1. Standard solutions
    2. Dilution calculations
    3. Solution preparation

    **Applications:**
    - Laboratory solution preparation
    - Chemical analysis
    - Industrial processes
    """)

    # Quiz for Molarity
    st.subheader("Test Your Knowledge! 📝")
    question = st.radio("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?", ["0.5 M", "1.0 M", "2.0 M", "4.0 M"])
    if st.button("Submit Answer"):
        st.write("The correct answer is: 4.0 M")
