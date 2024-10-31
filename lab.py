import streamlit as st

def lab():
    st.markdown("""
        <style>
        /* Glowing neon effect for title */
        @keyframes text-glow {
            0%, 100% { text-shadow: 0 0 8px #ff00ff, 0 0 16px #ff00ff, 0 0 32px #ff00ff; }
            50% { text-shadow: 0 0 12px #00ffff, 0 0 24px #00ffff, 0 0 48px #00ffff; }
        }
        .glowing-title {
            color: #ffffff;
            font-size: 3em;
            animation: text-glow 1.5s ease-in-out infinite alternate;
        }
        
        /* Beaker and pouring animation */
        .beaker {
            display: inline-block;
            width: 140px;
            height: 200px;
            border: 5px solid #ddd;
            border-radius: 0 0 20px 20px;
            background: transparent;
            position: relative;
            overflow: hidden;
        }
        
        /* Powder pouring for baking soda and sodium */
        .powder-pour {
            position: absolute;
            top: -50px;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 40px;
            background: #fff;
            border: 2px solid #999;
            animation: tilt-pour 3s forwards;
        }
        @keyframes tilt-pour {
            0% { transform: translateX(-50%) rotate(0deg); }
            50% { transform: translateX(-50%) rotate(45deg); }
            100% { transform: translateX(-50%) rotate(0deg); }
        }
        
        /* Bubble effect for vinegar and baking soda */
        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 1.5s infinite;
        }
        @keyframes rise {
            0% { transform: translateY(0); opacity: 0.9; }
            100% { transform: translateY(-120px); opacity: 0; }
        }
        
        /* Explosion and fire effect */
        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 100px;
            height: 100px;
            opacity: 0;
            background: radial-gradient(circle, #ff8800 0%, #ff4400 30%, transparent 70%);
            transform: translate(-50%, -50%);
            animation: explode 2s forwards;
        }
        @keyframes explode {
            0% { transform: scale(0); opacity: 0; }
            50% { transform: scale(2); opacity: 1; }
            100% { transform: scale(3); opacity: 0; }
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<h1 class="glowing-title" style="text-align: center;">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='height: 50%; background: rgba(255,255,255,0.8);'></div>
                <div class='powder-pour'></div>
                <div class='bubble' style='left: 20px; animation-delay: 0s;'></div>
                <div class='bubble' style='left: 50px; animation-delay: 0.5s;'></div>
                <div class='bubble' style='left: 80px; animation-delay: 1s;'></div>
            </div>
        """, unsafe_allow_html=True)
        st.write("Step 1: Slowly adding baking soda to vinegar solution...")
        st.write("Step 2: Observing the vigorous bubble formation...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='height: 50%; background: rgba(173,216,230,0.7);'></div>
                <div class='powder-pour'></div>
                <div class='explosion'></div>
            </div>
        """, unsafe_allow_html=True)
        st.write("Step 1: Carefully adding sodium to water...")
        st.write("Step 2: Observing the violent reaction...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) + Energy")
        
    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker'>
                    <div class='liquid' style='height: 50%; background: rgba(255,255,255,0.95);'></div>
                    <div class='ph-strip acid'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='height: 50%; background: rgba(255,255,255,0.95);'></div>
                    <div class='ph-strip neutral'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='height: 50%; background: rgba(255,255,255,0.95);'></div>
                    <div class='ph-strip base'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Dipping black pH strips into solutions...")
        st.write("Step 2: Observing color changes:")
        st.write("- Acidic solution: Strip turns red")
        st.write("- Neutral solution: Strip turns green")
        st.write("- Basic solution: Strip turns blue")

if __name__ == "__main__":
    lab()
