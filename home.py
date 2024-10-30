import streamlit as st

def home():
    st.markdown("""
        <div class="hero-section">
            <h1 class="glowing-title">Welcome to your virtual chemistry learning environment!</h1>
        </div>
        
        <div class="instruction-cards">
            <div class="card">Select a section on the left side</div>
            <div class="card">Follow the instructions</div>
            <div class="card">Experiment and learn!</div>
        </div>

        <div class="feature-cards">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h2>Perform chemical calculations</h2>
                    </div>
                    <div class="flip-card-back">
                        <p>Engage in a range of calculations including pH, pOH, and molarity.</p>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h2>Watch simulated reactions</h2>
                    </div>
                    <div class="flip-card-back">
                        <p>Observe virtual reactions with a mix of compounds.</p>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h2>Learn chemistry concepts</h2>
                    </div>
                    <div class="flip-card-back">
                        <p>Explore in-depth explanations of essential chemistry concepts.</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Include custom CSS
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
