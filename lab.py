import streamlit as st

def lab():
    st.markdown(
        """
        <style>
        /* Glowing Title */
        @keyframes text-glow {
            0% { text-shadow: 0 0 10px #00e6e6, 0 0 20px #00e6e6, 0 0 30px #00e6e6, 0 0 40px #00e6e6, 0 0 70px #00e6e6, 0 0 80px #00e6e6, 0 0 100px #00e6e6, 0 0 150px #00e6e6; }
            100% { text-shadow: 0 0 5px #00e6e6, 0 0 10px #00e6e6, 0 0 15px #00e6e6, 0 0 20px #00e6e6, 0 0 35px #00e6e6, 0 0 40px #00e6e6, 0 0 50px #00e6e6, 0 0 75px #00e6e6; }
        }
        h1 {
            font-size: 3em;
            text-align: center;
            color: #00e6e6;
            animation: text-glow 2s ease-in-out infinite alternate;
        }
        
        /* Acid-Base Reaction: Baking Soda and Vinegar */
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
            background: rgba(255, 102, 102, 0.6);
            transition: all 0.5s;
        }

        /* Powder Container and Stream */
        .powder-container {
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

        /* Bubble Rising Animation */
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

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 1.5s infinite;
        }

        /* Sodium and Water Explosion */
        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 300px;
            transform: translate(-50%, -50%);
            opacity: 0;
            animation: explode 2s forwards;
            animation-delay: 3s;
            pointer-events: none;
        }

        .fire {
            position: absolute;
            bottom: 50%;
            left: 0;
            width: 100%;
            height: 60px;
            opacity: 0;
            animation: burn 2s infinite;
            animation-delay: 3s;
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

    # Title with Neon Effect
    st.markdown('<h1>Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        # Baking Soda and Vinegar Reaction with bubbles
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,102,102,0.6);'></div>
                <div class='powder-container'></div>
                <div class='powder-stream'></div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 10px; animation-delay: 0s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Slowly adding baking soda to vinegar solution...")
        st.write("Step 2: Observing the vigorous bubble formation...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        # Sodium and Water Reaction with explosion and sparks
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(173,216,230,0.6);'></div>
                <div class='explosion'></div>
                <div class='fire'></div>
                <div class='sparks'>
                    <div class='spark' style='--x-end: 120px; --y-end: -100px; animation-delay: 3.2s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Carefully adding sodium to water...")
        st.write("Step 2: Observing the violent reaction...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) + Energy")

if __name__ == "__main__":
    lab()
