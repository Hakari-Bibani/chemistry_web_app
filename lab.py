import streamlit as st
import time

def lab():
    st.markdown(
        """
        <style>
        /* Neon Title Effect */
        @keyframes text-glow {
            0%, 100% { text-shadow: 0 0 8px #ff007f, 0 0 20px #ff007f, 0 0 30px #ff007f, 0 0 40px #ff007f; }
            50% { text-shadow: 0 0 16px #ff00ff, 0 0 30px #ff00ff, 0 0 45px #ff00ff, 0 0 60px #ff00ff; }
        }
        .title {
            font-family: Arial, sans-serif;
            text-align: center;
            color: #ff007f;
            animation: text-glow 2s infinite alternate;
            margin-bottom: 2em;
        }

        /* General Beaker Styles */
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
        .liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 255, 255, 0.9);
            transition: all 0.5s;
        }
        
        /* Acid-Base Reaction: Pouring Baking Soda */
        .baking-soda-container {
            position: absolute;
            top: -80px;
            left: 50%;
            transform: translateX(-50%) rotate(-5deg);
            width: 40px;
            height: 60px;
            background: #fff;
            border: 2px solid #999;
            animation: tilt-pour 3s forwards;
            transform-origin: bottom right;
        }
        .baking-soda-stream {
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
        
        /* Exothermic Reaction: Pouring Sodium and Explosion */
        .explosion { /* similar to your initial style */ }
        .spark { /* similar to your initial style */ }
        .fire { /* similar to your initial style */ }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    # Acid-Base Reaction with Baking Soda and Vinegar
    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255, 0, 0, 0.3);'></div>
                <div class='baking-soda-container'></div>
                <div class='baking-soda-stream'></div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 10px; animation-delay: 0s;'></div>
                    <!-- Additional bubbles similar to your initial style -->
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Slowly adding baking soda to vinegar solution...")
        st.write("Step 2: Observing the vigorous bubble formation...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    # Exothermic Reaction with Sodium and Water
    elif reaction_type == "E
