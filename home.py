import streamlit as st

def home():
    # Apply custom CSS for the homepage
    st.markdown("""
        <style>
        /* Hero Section - Neon Effect */
        .hero-title {
            font-size: 2.5em;
            text-align: center;
            color: #FFF;
            animation: text-glow 2s ease-in-out infinite alternate;
        }
        
        /* Text Glow Animation */
        @keyframes text-glow {
            from { text-shadow: 0 0 10px #00e5ff, 0 0 20px #00e5ff, 0 0 30px #00e5ff; }
            to { text-shadow: 0 0 20px #00e5ff, 0 0 30px #00e5ff, 0 0 40px #00e5ff, 0 0 50px #00e5ff; }
        }
        
        /* Cards for instructions */
        .card {
            display: inline-block;
            width: 18%;
            margin: 10px;
            padding: 20px;
            text-align: center;
            border: 2px solid #00e5ff;
            border-radius: 10px;
            color: #FFF;
            cursor: pointer;
            background-color: rgba(255, 255, 255, 0.1);
            transition: transform 0.3s ease;
        }
        
        .card:hover {
            transform: scale(1.05);
            background-color: rgba(255, 255, 255, 0.2);
        }

        /* 3D Flip Card Container */
        .flip-card {
            background-color: transparent;
            width: 200px;
            height: 300px;
            perspective: 1000px;
            display: inline-block;
            margin: 20px;
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

        /* Front and Back Faces of Flip Cards */
        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 10px;
            padding: 20px;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2em;
        }

        .flip-card-front {
            background-color: #00e5ff;
        }

        .flip-card-back {
            background-color: #003366;
            transform: rotateY(180deg);
        }
        </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown('<h1 class="hero-title">Welcome to your virtual chemistry learning environment!</h1>', unsafe_allow_html=True)

    # Instruction Cards
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Select a section on the left side</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Follow the instructions</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Experiment and learn!</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 3D Flip Cards for Features
    st.markdown("<div style='text-align: center; display: flex; justify-content: center; gap: 20px;'>", unsafe_allow_html=True)

    st.markdown("""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    Perform Chemical Calculations
                </div>
                <div class="flip-card-back">
                    Dive deep into calculations for pH, molarity, and other key concepts!
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    Watch Simulated Reactions
                </div>
                <div class="flip-card-back">
                    Explore virtual lab simulations of various chemical reactions.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    Learn Chemistry Concepts
                </div>
                <div class="flip-card-back">
                    Access detailed explanations and test your knowledge on key topics.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Run the home function when this script is executed
if __name__ == "__main__":
    home()
