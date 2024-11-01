import streamlit as st

def main():
    st.title("Virtual Chemistry Lab 🧪")

    # Reaction selection
    reaction_type = st.selectbox("Choose a reaction:", ["Select a reaction", "Acid-Base (baking soda & vinegar)"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown('<h2 style="text-align: center;">Baking Soda and Vinegar Reaction Simulator</h2>', unsafe_allow_html=True)

        st.markdown("""
            <style>
                .beaker {
                    position: relative;
                    width: 100px;
                    height: 200px;
                    background: #ccc;
                    border-radius: 10px 10px 0 0;
                    overflow: hidden;
                    margin: 0 auto;
                }

                .liquid {
                    position: absolute;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    height: 50%; /* Adjust this to fill more or less */
                    background: rgba(255, 99, 71, 0.5); /* Translucent light red */
                    animation: swirl 5s infinite;
                }

                @keyframes swirl {
                    0% { transform: rotate(0deg); }
                    50% { transform: rotate(3deg); }
                    100% { transform: rotate(0deg); }
                }

                .spoon {
                    position: absolute;
                    right: 50px;
                    top: 40%;
                    transform: translateY(-50%);
                }

                .powder-stream {
                    position: absolute;
                    top: 40px;
                    left: 50%;
                    width: 6px;
                    height: 0;
                    background: rgba(255, 255, 255, 0.9);
                    animation: pour-powder 3s forwards;
                    filter: blur(1px);
                    transform-origin: top center;
                }

                @keyframes pour-powder {
                    0% { height: 0; opacity: 0; }
                    20% { height: 80px; opacity: 1; }
                    80% { height: 80px; opacity: 1; }
                    100% { height: 0; opacity: 0; }
                }

                .bubbles {
                    position: absolute;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    opacity: 0;
                    animation: show-bubbles 4s forwards;
                    animation-delay: 2s;
                }

                @keyframes show-bubbles {
                    0% { opacity: 0; }
                    100% { opacity: 1; }
                }

                .bubble {
                    position: absolute;
                    background: rgba(200, 200, 200, 0.5);  /* Light gray bubbles */
                    border-radius: 50%;
                    animation: rise 1.5s infinite;
                }

                @keyframes rise {
                    0% { transform: translateY(0); opacity: 1; }
                    100% { transform: translateY(-120px); opacity: 0; }
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class='beaker'>
                <div class='liquid'></div>
                <div class='powder-stream'></div>
                <div class='bubbles'></div>
            </div>
            <div class='spoon'>
                <div style='width: 20px; height: 5px; background: white; border-radius: 10px;'></div>
                <div style='width: 30px; height: 30px; background: #fff; border-radius: 50%; margin-top: -10px;'></div> <!-- Spoon and powder -->
            </div>
        """, unsafe_allow_html=True)

        if st.button('Start Reaction'):
            # Start the pouring animation
            st.markdown("""
                <script>
                const powderStream = document.querySelector('.powder-stream');
                powderStream.style.animation = 'pour-powder 3s forwards';
                </script>
            """, unsafe_allow_html=True)

            # Trigger the bubbles animation
            st.markdown("""
                <script>
                const bubbles = document.querySelector('.bubbles');
                bubbles.style.animation = 'show-bubbles 4s forwards';
                </script>
            """, unsafe_allow_html=True)

            st.write("Step 1: Slowly adding baking soda to vinegar solution...")
            st.write("Step 2: Observing the vigorous bubble formation...")
            st.write("Chemical Reaction: NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

if __name__ == "__main__":
    main()
