import streamlit as st

def home():
    # Main Container for the Home Page
    st.markdown("""
    <style>
        /* Hero Section: Neon Title */
        .hero-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #00e5ff;
            animation: text-glow 1.5s ease-in-out infinite alternate;
            text-align: center;
            margin-top: 20px;
        }
        
        /* Neon Glow Animation */
        @keyframes text-glow {
            0% {
                text-shadow: 0 0 5px #00e5ff, 0 0 10px #00e5ff, 0 0 15px #00e5ff, 0 0 20px #00e5ff;
            }
            100% {
                text-shadow: 0 0 20px #00e5ff, 0 0 30px #00e5ff, 0 0 40px #00e5ff, 0 0 50px #00e5ff;
            }
        }

        /* Styled Instruction Cards */
        .card-container {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 20px;
        }
        
        .card {
            width: 200px;
            padding: 20px;
            background-color: #f0f8ff;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s;
        }
        
        .card:hover {
            transform: scale(1.05);
        }

        /* Flip Card Container */
        .flip-card-container {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 40px;
        }

        /* 3D Flip Cards */
        .flip-card {
            width: 200px;
            height: 200px;
            perspective: 1000px;
        }

        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }

        .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg);
        }

        .flip-front, .flip-back {
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            color: white;
        }

        .flip-front {
            background-color: #4CAF50;
        }

        .flip-back {
            background-color: #333;
            transform: rotateY(180deg);
        }

    </style>

    <div class="hero-title">
        Welcome to your virtual chemistry learning environment!
    </div>

    <div class="card-container">
        <div class="card">Select a section on the left side</div>
        <div class="card">Follow the instructions</div>
        <div class="card">Experiment and learn!</div>
    </div>

    <div class="flip-card-container">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-front">
                    <p>Perform Chemical Calculations</p>
                </div>
                <div class="flip-back">
                    <p>Access various tools to calculate pH, molarity, and more!</p>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-front">
                    <p>Watch Simulated Reactions</p>
                </div>
                <div class="flip-back">
                    <p>Explore virtual reactions and see chemistry in action.</p>
                </div>
            </div>
        </div>

        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-front">
                    <p>Learn Chemistry Concepts</p>
                </div>
                <div class="flip-back">
                    <p>Dive deep into explanations and principles of chemistry.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
