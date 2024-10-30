import streamlit as st

def home_page():
    st.title("Welcome to your virtual chemistry learning environment!")
    st.markdown("""
        <div class="glowing-title">Welcome to your virtual chemistry learning environment!</div>
        """, unsafe_allow_html=True)
    
    # Displaying what you can do
    st.markdown("<h3>📚 What you can do here:</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class="instruction-cards">
            <div class="card">Perform chemical calculations</div>
            <div class="card">Watch simulated reactions</div>
            <div class="card">Learn chemistry concepts</div>
        </div>
    """, unsafe_allow_html=True)

    # Getting Started Section
    st.markdown("<h3>🔬 Getting Started:</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class="instruction-cards">
            <div class="card">Select a section on the left side</div>
            <div class="card">Follow the instructions</div>
            <div class="card">Experiment and learn!</div>
        </div>
    """, unsafe_allow_html=True)

    # Adding flip cards for features
    st.markdown("""
        <div class="feature-cards">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">Perform chemical calculations</div>
                    <div class="flip-card-back">Details about calculations.</div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">Watch simulated reactions</div>
                    <div class="flip-card-back">Details about reactions.</div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">Learn chemistry concepts</div>
                    <div class="flip-card-back">Details about concepts.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main function to control the app's flow
def main():
    # Only show the home page
    home_page()

if __name__ == "__main__":
    main()
