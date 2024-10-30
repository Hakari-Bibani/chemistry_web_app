import streamlit as st

# Define the title and description for the home page
st.markdown('<h1 class="glowing-title">Welcome to your virtual chemistry learning environment!</h1>', unsafe_allow_html=True)

# Instruction section
st.markdown('<h2>📚 What you can do here:</h2>', unsafe_allow_html=True)

# Horizontal instruction cards
st.markdown("""
<div class="instruction-cards">
    <div class="card">Perform chemical calculations</div>
    <div class="card">Watch simulated reactions</div>
    <div class="card">Learn chemistry concepts</div>
</div>
""", unsafe_allow_html=True)

# Flip cards section
st.markdown('<h2>Explore Features:</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="feature-cards">
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h3>Perform Chemical Calculations</h3>
            </div>
            <div class="flip-card-back">
                <p>Learn how to calculate pH, molarity, and more!</p>
            </div>
        </div>
    </div>
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h3>Watch Simulated Reactions</h3>
            </div>
            <div class="flip-card-back">
                <p>Observe chemical reactions in a virtual environment!</p>
            </div>
        </div>
    </div>
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h3>Learn Chemistry Concepts</h3>
            </div>
            <div class="flip-card-back">
                <p>Deepen your understanding of essential chemistry topics!</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Instructions to the user
st.markdown("""
<h2>🔬 Getting Started:</h2>
<ul>
    <li>Select a section on the left side</li>
    <li>Follow the instructions</li>
    <li>Experiment and learn!</li>
</ul>
""", unsafe_allow_html=True)
