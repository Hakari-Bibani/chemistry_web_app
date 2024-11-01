import streamlit as st
import time

def lab():
    st.markdown(
        """
        <style>
        .beaker {
            display: inline-block;
            width: 140px;
            height: 200px;
            border: 5px solid #ddd;
            border-radius: 0 0 20px 20px;
            position: relative;
            margin: 40px;
            background: transparent;
            overflow: hidden;
            box-shadow: inset 0 0 20px rgba(255,255,255,0.2);
        }

        .beaker .liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 100, 100, 0.7); /* light red liquid */
            transition: transform 0.5s;
            animation: swirl 4s infinite linear; /* gentle swirling animation */
        }

        @keyframes swirl {
            0% { transform: rotate(0deg); }
            50% { transform: rotate(1deg); }
            100% { transform: rotate(0deg); }
        }

        .spoon {
            position: absolute;
            top: -40px;
            right: -20px;
            width: 50px;
            height: 20px;
            background: #333; /* black spoon */
            clip-path: polygon(0 0, 100% 0, 75% 100%, 25% 100%);
            transform: rotate(-15deg);
        }

        .powder {
            position: absolute;
            top: 5px;
            left: 5px;
            width: 15px;
            height: 10px;
            background: #fff;
            filter: blur(1px);
            border-radius: 3px;
            animation: pour-powder 3s forwards;
            opacity: 0;
        }

        @keyframes pour-powder {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(100px); opacity: 0; } /* pour powder down */
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            height: 100%;
            opacity: 0;
            animation: bubble-rise 3s forwards;
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 1.5s infinite;
        }

        @keyframes bubble-rise {
            0% { opacity: 0; }
            20% { opacity: 1; }
            100% { opacity: 1; }
        }

        .reaction-bubbles .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 2s infinite;
        }

        @keyframes rise {
            0% { transform: translateY(0) translateX(var(--x-start)); opacity: 0.8; width: var(--size); height: var(--size); }
            100% { transform: translateY(-120px) translateX(var(--x-end)); opacity: 0; width: calc(var(--size) * 2); height: calc(var(--size) * 2); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 style="text-align: center; margin-bottom: 2em;">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Baking Soda and Vinegar Reaction Simulator")
    
    # Display "Start Reaction" button
    if st.button("Start Reaction"):
        st.markdown("""
            <div class='beaker'>
                <div class='liquid'></div>
                <div class='spoon'>
                    <div class='powder'></div> <!-- Powder falling effect -->
                </div>
                <div class='bubbles'>
                    <!-- Dynamic bubbles that rise during the reaction -->
                    <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 10px;'></div>
                    <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 15px;'></div>
                    <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 12px;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: The baking soda gradually pours into the vinegar.")
        st.write("Step 2: Vigorous fizzing reaction as the vinegar solution becomes agitated.")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

if __name__ == "__main__":
    lab()
