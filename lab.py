import streamlit as st
import time

def lab():
    # Enhanced CSS with more realistic animations
    st.markdown(
        """
        <style>
        .glowing-title {
            font-size: 2.5em;
            color: black;
            text-align: center;
            text-shadow: 0 0 10px #add8e6, 0 0 20px #add8e6;
            animation: text-glow 1.5s infinite alternate;
        }
        
        @keyframes text-glow {
            from { text-shadow: 0 0 5px #add8e6, 0 0 10px #add8e6; }
            to { text-shadow: 0 0 20px #add8e6, 0 0 30px #add8e6; }
        }

        .beaker {
            display: inline-block;
            width: 120px;
            height: 180px;
            border: 4px solid #999;
            border-radius: 0 0 20px 20px;
            position: relative;
            margin: 20px;
            background: linear-gradient(to bottom, #ffffff00, #ffffff40);
            overflow: hidden;
        }

        .beaker::before {
            content: '';
            position: absolute;
            top: -10px;
            left: -10px;
            right: -10px;
            height: 20px;
            background: #999;
            border-radius: 5px;
        }

        .liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 80%;
            background: rgba(255, 255, 255, 0.8);
            transition: background-color 2s;
        }

        .powder {
            position: absolute;
            top: -30px;
            left: 50%;
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
            opacity: 0;
            animation: fall 2s forwards;
        }

        @keyframes fall {
            0% { transform: translateY(0) translateX(-50%); opacity: 1; }
            100% { transform: translateY(200px) translateX(-50%); opacity: 0; }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }

        .bubble {
            position: absolute;
            bottom: 0;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 2s infinite;
        }

        @keyframes rise {
            0% { 
                transform: translateY(0) translateX(0);
                opacity: 0.8;
            }
            100% { 
                transform: translateY(-180px) translateX(var(--x-offset));
                opacity: 0;
            }
        }

        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 200px;
            height: 200px;
            opacity: 0;
            pointer-events: none;
        }

        .explosion.active {
            animation: explode 1s forwards;
        }

        @keyframes explode {
            0% { 
                transform: translate(-50%, -50%) scale(0);
                opacity: 1;
                background: radial-gradient(circle, #ff4400 0%, #ff000000 70%);
            }
            100% { 
                transform: translate(-50%, -50%) scale(2);
                opacity: 0;
                background: radial-gradient(circle, #ff440000 0%, #ff000000 100%);
            }
        }

        .ph-strip {
            position: absolute;
            width: 10px;
            height: 80px;
            background: #fff;
            left: 50%;
            transform-origin: bottom center;
            animation: dip 4s forwards;
        }

        @keyframes dip {
            0% { transform: translateX(-50%) translateY(-100%) rotate(0deg); }
            25% { transform: translateX(-50%) translateY(50%) rotate(0deg); }
            75% { transform: translateX(-50%) translateY(50%) rotate(0deg); }
            100% { transform: translateX(-50%) translateY(-100%) rotate(0deg); }
        }

        .sparks {
            position: absolute;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }

        .spark {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #ff4400;
            border-radius: 50%;
            animation: spark 0.8s linear forwards;
        }

        @keyframes spark {
            0% { transform: translate(0, 0); opacity: 1; }
            100% { transform: translate(var(--x-end), var(--y-end)); opacity: 0; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the title
    st.markdown('<h1 class="glowing-title">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    # Selection for reaction type
    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,255,255,0.8);'></div>
                <div class='powder'></div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-offset: 10px; animation-delay: 0s;'></div>
                    <div class='bubble' style='--x-offset: -15px; animation-delay: 0.5s;'></div>
                    <div class='bubble' style='--x-offset: 5px; animation-delay: 1s;'></div>
                    <div class='bubble' style='--x-offset: -10px; animation-delay: 1.5s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding baking soda (NaHCO₃) to vinegar (CH₃COOH)...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,255,255,0.9);'></div>
                <div class='powder'></div>
                <div class='explosion'></div>
                <div class='sparks'>
                    <div class='spark' style='--x-end: 50px; --y-end: -50px;'></div>
                    <div class='spark' style='--x-end: -30px; --y-end: -40px;'></div>
                    <div class='spark' style='--x-end: 20px; --y-end: -60px;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")
        
    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker' style='background: rgba(255,0,0,0.1);'>
                    <div class='liquid' style='background: rgba(255,0,0,0.1);'></div>
                    <div class='ph-strip' style='animation-delay: 0s;'></div>
                </div>
                <div class='beaker' style='background: rgba(0,255,0,0.1);'>
                    <div class='liquid' style='background: rgba(0,255,0,0.1);'></div>
                    <div class='ph-strip' style='animation-delay: 4s;'></div>
                </div>
                <div class='beaker' style='background: rgba(0,0,255,0.1);'>
                    <div class='liquid' style='background: rgba(0,0,255,0.1);'></div>
                    <div class='ph-strip' style='animation-delay: 8s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Testing pH levels in different solutions...")
        st.write("Watch the pH strips change color:")
        st.write("Red: Acidic (pH < 7)")
        st.write("Green: Neutral (pH = 7)")
        st.write("Blue: Basic (pH > 7)")

if __name__ == "__main__":
    lab()
