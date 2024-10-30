import streamlit as st
from streamlit.components.v1 import html

def home():
    # Main Content
    st.markdown("""
        <style>
            /* Background Gradient */
            body {
                background: linear-gradient(to bottom right, #00c6ff, #0072ff);
                color: white;
            }

            /* Content Box Styling */
            .content-box {
                background-color: rgba(255, 255, 255, 0.2);
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                text-align: center;
            }

            /* Header Text with Animation */
            .header-text {
                font-family: Arial, sans-serif;
                font-size: 2em;
                animation: fadeIn 2s ease-in-out;
            }

            /* Keyframes for Fade In Animation */
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }

            /* Styled Buttons for Sections */
            .section-button {
                display: inline-block;
                background-color: #ff7e5f;
                padding: 15px 25px;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                margin: 10px;
                cursor: pointer;
                transition: transform 0.3s ease;
            }

            .section-button:hover {
                transform: scale(1.1);
                background-color: #feb47b;
            }
        </style>

        <div class="content-box">
            <div class="header-text">Welcome to your virtual chemistry learning environment!</div>
            <div style="margin-top: 10px;">
                <p>Explore the magic and complexity of chemistry through interactive tools and simulations.</p>
            </div>
        </div>

        <div class="content-box">
            <h2 class="header-text">📚 What you can do here</h2>
            <div class="section-button">Perform chemical calculations</div>
            <div class="section-button">Watch simulated reactions</div>
            <div class="section-button">Learn chemistry concepts</div>
        </div>

        <div class="content-box">
            <h2 class="header-text">🔬 Getting Started</h2>
            <div>
                <p>1. Select a section on the left side</p>
                <p>2. Follow the instructions</p>
                <p>3. Experiment and learn!</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
