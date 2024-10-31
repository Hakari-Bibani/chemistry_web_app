import streamlit as st
import time

def lab():
    st.markdown(
        """
        <style>
        /* Neon glowing effect for title */
        @keyframes text-glow {
            0%, 100% { color: #fff; text-shadow: 0 0 8px #08f, 0 0 20px #08f, 0 0 30px #08f; }
            50% { color: #08f; text-shadow: 0 0 12px #08f, 0 0 30px #08f, 0 0 45px #08f; }
        }
        
        h1.neon {
            animation: text-glow 2s infinite ease-in-out;
            text-align: center;
            font-weight: bold;
        }

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

        /* Baking Soda & Vinegar Simulation */
        .vinegar-liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 100, 100, 0.5); /* Light red */
            transition: all 0.5s;
        }

        .powder-container, .powder-stream {
            position: absolute;
            top: -50px;
            left: 50%;
            width: 30px;
            height: 50px;
            background: #ddd;
            transform: translateX(-50%) rotate(-5deg);
            border-radius: 5px;
        }

        @keyframes pour-powder {
            0%, 20% { height: 0; opacity: 0; }
            20% { height: 70px; opacity: 1; }
            80% { height: 70px; opacity: 1; }
            100% { height: 0; opacity: 0; }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            animation: show-bubbles 2s forwards;
            animation-delay: 3s;
        }

        /* Sodium and Water Explosion Effect */
        .water-liquid {
            background: rgba(100, 200, 255, 0.5); /* Light blue water */
        }

        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 300px;
            transform: translate(-50%, -50%);
            opacity: 0;
            animation: explode 2s forwards;
            animation-delay: 4s;
        }

        .fire {
            position: absolute;
            bottom: 50%;
            left: 0;
            width: 100%;
            height: 60px;
            opacity: 0;
            animation: burn 2s infinite;
            animation-delay: 3.5s;
            filter: blur(2px);
            transform-origin: center bottom;
        }

        .spark {
            position: absolute;
            width: 8px;
            height: 8px;
            background: #ff8800;
            border-radius: 50%;
            filter: blur(2px);
            opacity: 0;
            animation: spark 1s linear forwards;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="neon">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='vinegar-liquid'></div>
                <div class='powder-container'></div>
                <div class='powder-stream'></div>
                <div class='bubbles'>
                    <!-- Multiple divs for bubbles rising up -->
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Slowly adding baking soda to vinegar solution...")
        st.write("Step 2: Observing the vigorous bubble formation...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='water-liquid'></div>
                <div class='explosion'></div>
                <div class='fire'></div>
                <div class='sparks'>
                    <div class='spark' style='--x-end: 120px; --y-end: -100px; animation-delay: 3.2s;'></div>
                    <div class='spark' style='--x-end: -100px; --y-end: -80px; animation-delay: 3.4s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Carefully adding sodium to water...")
        st.write("Step 2: Observing the violent reaction...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) + Energy")
    
if __name__ == "__main__":
    lab()
