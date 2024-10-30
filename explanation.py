import streamlit as st

def explanations():
    # Update only the CSS part with new animations
    st.markdown("""
        <style>
        @keyframes text-glow {
            0% { 
                text-shadow: 0 0 10px #fff, 0 0 20px #2377ff, 0 0 30px #2377ff;
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-10px);
            }
            100% { 
                text-shadow: 0 0 20px #fff, 0 0 30px #00bfff, 0 0 40px #00bfff;
                transform: translateY(0px);
            }
        }
        
        .glowing-title {
            text-align: center;
            color: #000;  /* Changed to black */
            font-size: 2.5em;
            animation: text-glow 3s ease-in-out infinite;
            margin-bottom: 2em;
            font-weight: bold;
        }
        
        @keyframes card-float {
            0% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-5px);
            }
            100% {
                transform: translateY(0px);
            }
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
            animation: card-float 3s ease-in-out infinite;
            flex: 1;
        }
        
        .topic-card:hover {
            animation: none;
            transform: translateY(-8px);
            box-shadow: 0 5px 15px rgba(35, 119, 255, 0.3);
        }
        
        /* Keep the rest of your CSS unchanged */
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
