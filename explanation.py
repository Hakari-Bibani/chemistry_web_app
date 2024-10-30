import streamlit as st

def explanations():
    # Custom CSS with animations and styling
    st.markdown("""
        <style>
        /* Glowing title animation */
        @keyframes text-glow {
            0% { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #2196F3, 0 0 40px #2196F3; }
            100% { text-shadow: 0 0 20px #fff, 0 0 30px #08a6ff, 0 0 40px #08a6ff, 0 0 50px #08a6ff; }
        }
        
        .glowing-title {
            text-align: center;
            color: #fff;
            font-size: 2.5rem;
            font-weight: bold;
            animation: text-glow 1.5s ease-in-out infinite alternate;
            margin-bottom: 2rem;
            padding: 20px;
            background: linear-gradient(45deg, #1a1a1a, #2c2c2c);
            border-radius: 10px;
        }
        
        /* Topic cards container */
        .topic-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin: 2rem 0;
        }
        
        /* Topic card styling */
        .topic-card {
            background: linear-gradient(145deg, #2196F3, #21CBF3);
            border-radius: 15px;
            padding: 20px;
            width: 200px;
            text-align: center;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        
        .topic-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(33, 150, 243, 0.3);
        }
        
        .topic-card h3 {
            color: white;
            margin: 0;
            font-size: 1.5rem;
        }
        
        /* Quiz styling */
        .quiz-container {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 20px;
            margin-top: 2rem;
        }
        
        .quiz-option {
            background: #2196F3;
            color: white;
            padding: 10px 20px;
            margin: 5px 0;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        .quiz-option:hover {
            background: #1976D2;
        }
        
        .correct-answer {
            background: #4CAF50 !important;
        }
        
        .wrong-answer {
            background: #F44336 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Animated title
    st.markdown('<h1 class="glowing-title">📚 Chemistry Concepts & Explanation</h1>', unsafe_allow_html=True)

    # Topic cards in horizontal row
    st.markdown("""
        <div class="topic-container">
            <div class="topic-card" onclick="selectTopic('pH')">
                <h3>pH</h3>
            </div>
            <div class="topic-card" onclick="selectTopic('pOH')">
                <h3>pOH</h3>
            </div>
            <div class="topic-card" onclick="selectTopic('Molarity')">
                <h3>Molarity</h3>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Topic selection using streamlit (behind the scenes)
    topic = st.selectbox("", ["", "pH", "pOH", "Molarity"], label_visibility="collapsed")

    if topic == "pH":
        st.markdown("""
            <div style='background: rgba(33, 150, 243, 0.1); padding: 20px; border-radius: 10px; margin: 20px 0;'>
                <h2 style='color: #2196F3;'>Understanding pH</h2>
                <p><strong>What is pH?</strong><br>
                pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.</p>
                
                <h3>The pH Scale:</h3>
                <ul>
                    <li>pH < 7: Acidic</li>
                    <li>pH = 7: Neutral</li>
                    <li>pH > 7: Basic (Alkaline)</li>
                </ul>
                
                <p><strong>Calculating pH:</strong><br>
                pH = -log[H⁺] where [H⁺] is the concentration of hydrogen ions in mol/L</p>
                
                <h3>Common Examples:</h3>
                <ul>
                    <li>Lemon juice: pH 2 (acidic)</li>
                    <li>Pure water: pH 7 (neutral)</li>
                    <li>Baking soda: pH 9 (basic)</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        # Quiz section
        st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
        st.subheader("🎯 Test Your Knowledge!")
        
        # Store the user's answer in session state
        if 'ph_answer' not in st.session_state:
            st.session_state.ph_answer = None
            st.session_state.ph_submitted = False

        answer = st.radio(
            "What pH value represents a neutral solution?",
            ("0", "7", "14", "3.5")
        )

        if st.button("Submit Answer"):
            st.session_state.ph_answer = answer
            st.session_state.ph_submitted = True

        if st.session_state.ph_submitted:
            if st.session_state.ph_answer == "7":
                st.success("🎉 Correct! A neutral solution has a pH of 7.")
            else:
                st.error("❌ That's incorrect. The correct answer is 7.")
                st.info("Explanation: A pH of 7 represents a neutral solution where the concentration of H+ ions equals the concentration of OH- ions.")

    elif topic == "pOH":
        # Similar structure for pOH content and quiz
        st.markdown("""
            <div style='background: rgba(33, 150, 243, 0.1); padding: 20px; border-radius: 10px; margin: 20px 0;'>
                <h2 style='color: #2196F3;'>Understanding pOH</h2>
                <!-- pOH content -->
            </div>
        """, unsafe_allow_html=True)
        # Add pOH quiz similar to pH quiz

    elif topic == "Molarity":
        # Similar structure for Molarity content and quiz
        st.markdown("""
            <div style='background: rgba(33, 150, 243, 0.1); padding: 20px; border-radius: 10px; margin: 20px 0;'>
                <h2 style='color: #2196F3;'>Understanding Molarity</h2>
                <!-- Molarity content -->
            </div>
        """, unsafe_allow_html=True)
        # Add Molarity quiz similar to pH quiz

if __name__ == "__main__":
    explanations()
