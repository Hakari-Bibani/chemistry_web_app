import streamlit as st

def explanations():
    # Add custom CSS with animation and card styling
    import streamlit as st

def explanations():
    # Add custom CSS with animation and card styling
    st.markdown("""
        <style>
        @keyframes text-glow {
            0% { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #2377ff, 0 0 40px #2377ff; }
            100% { text-shadow: 0 0 20px #fff, 0 0 30px #00bfff, 0 0 40px #00bfff, 0 0 50px #00bfff; }
        }
        
        .glowing-title {
            text-align: center;
            color: #fff;
            font-size: 2.5em;
            animation: text-glow 1.5s ease-in-out infinite alternate;
            margin-bottom: 2em;
        }
        
        .topic-cards {
            display: flex;
            justify-content: space-around;
            gap: 20px;
            margin: 2em 0;
        }
        
        .topic-card {
            background: linear-gradient(145deg, #2377ff22, #00bfff22);
            border: 2px solid #2377ff;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            flex: 1;
        }
        
        .topic-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(35, 119, 255, 0.3);
        }
        
        .quiz-section {
            background: rgba(35, 119, 255, 0.1);
            border-radius: 10px;
            padding: 20px;
            margin-top: 2em;
        }
        
        .quiz-title {
            color: #2377ff;
            text-align: center;
            font-size: 1.5em;
            margin-bottom: 1em;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Glowing animated title
    st.markdown('<h1 class="glowing-title">📚 Chemistry Concepts & Explanation</h1>', unsafe_allow_html=True)
    
    # Topic cards in horizontal layout
    st.markdown("""
        <div class="topic-cards">
            <div class="topic-card" onclick="document.querySelector('#topic-select').value='pH'">
                <h3>pH</h3>
                <p>Learn about acidity and basicity</p>
            </div>
            <div class="topic-card" onclick="document.querySelector('#topic-select').value='pOH'">
                <h3>pOH</h3>
                <p>Explore hydroxide concentration</p>
            </div>
            <div class="topic-card" onclick="document.querySelector('#topic-select').value='Molarity'">
                <h3>Molarity</h3>
                <p>Understand solution concentration</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Topic selection with the same options
    topic = st.selectbox("Choose a topic:", ["", "pH", "pOH", "Molarity"], key="topic-select")
    
    if topic == "pH":
        st.subheader("Understanding pH")
        st.write("""
            **What is pH?**
            pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.
            
            **The pH Scale:**
            - pH < 7: Acidic
            - pH = 7: Neutral
            - pH > 7: Basic (Alkaline)
        """)
        
        # Enhanced quiz section
        st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
        st.markdown('<h3 class="quiz-title">Test Your Knowledge! 📝</h3>', unsafe_allow_html=True)
        
        user_answer = st.radio(
            "What pH value represents a neutral solution?",
            ("0", "7", "14", "3.5")
        )
        
        if st.button("Check Answer"):
            if user_answer == "7":
                st.success("🎉 Correct! A neutral solution has a pH of 7.")
                st.write("Explanation: At pH 7, the concentration of H+ ions equals OH- ions.")
            else:
                st.error("That's not quite right. Try again!")
                if st.button("Show Correct Answer"):
                    st.info("The correct answer is 7. At pH 7, the solution is neutral.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif topic == "pOH":
        # Similar structure for pOH content
        st.subheader("Understanding pOH")
        st.write("""
            **What is pOH?**
            pOH is a measure of the hydroxide ion concentration in a solution.
            
            **The pOH Scale:**
            - pOH < 7: Basic
            - pOH = 7: Neutral
            - pOH > 7: Acidic
        """)
        
        st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
        st.markdown('<h3 class="quiz-title">Test Your Knowledge! 📝</h3>', unsafe_allow_html=True)
        
        user_answer = st.radio(
            "If a solution has a pOH of 3, is it acidic or basic?",
            ("Acidic", "Basic", "Neutral")
        )
        
        if st.button("Check Answer"):
            if user_answer == "Basic":
                st.success("🎉 Correct! A solution with pOH = 3 is basic.")
                st.write("Explanation: pOH < 7 indicates a basic solution.")
            else:
                st.error("That's not quite right. Try again!")
                if st.button("Show Correct Answer"):
                    st.info("The correct answer is Basic. When pOH < 7, the solution is basic.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif topic == "Molarity":
        st.subheader("Understanding Molarity")
        st.write("""
            **What is Molarity?**
            Molarity (M) is a measure of the concentration of a solution.
            
            **Formula:**
            M = moles of solute / liters of solution
        """)
        
        st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
        st.markdown('<h3 class="quiz-title">Test Your Knowledge! 📝</h3>', unsafe_allow_html=True)
        
        user_answer = st.radio(
            "If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?",
            ("1.0 M", "2.0 M", "3.0 M", "4.0 M")
        )
        
        if st.button("Check Answer"):
            if user_answer == "4.0 M":
                st.success("🎉 Correct! The molarity is 4.0 M.")
                st.write("Explanation: M = 2 moles ÷ 0.5 L = 4.0 M")
            else:
                st.error("That's not quite right. Try again!")
                if st.button("Show Correct Answer"):
                    st.info("The correct answer is 4.0 M. Calculated as: 2 moles ÷ 0.5 L = 4.0 M")
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    explanations()
