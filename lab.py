import streamlit as st
import time

def lab():
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
            width: 140px;
            height: 200px;
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
            height: 50%;
            transition: all 2s;
        }

        .liquid.vinegar {
            background: rgba(255, 0, 0, 0.3);
            animation: move-liquid 2s infinite alternate;
        }

        .liquid.water {
            background: rgba(173, 216, 230, 0.5);
            animation: move-liquid 2s infinite alternate;
        }

        @keyframes move-liquid {
            0%, 100% { transform: translateX(-5px); }
            50% { transform: translateX(5px); }
        }

        .powder-stream {
            position: absolute;
            top: -30px;
            left: 50%;
            width: 4px;
            height: 100px;
            background: repeating-linear-gradient(
                white 0%,
                white 20%,
                transparent 20%,
                transparent 80%
            );
            animation: pour-powder 3s forwards;
            opacity: 0;
        }

        @keyframes pour-powder {
            0% { opacity: 0; transform: translateX(-50%) rotate(0deg); }
            10% { opacity: 1; transform: translateX(-50%) rotate(0deg); }
            90% { opacity: 1; transform: translateX(-50%) rotate(0deg); }
            100% { opacity: 0; transform: translateX(-50%) rotate(0deg); }
        }

        .bubble {
            position: absolute;
            background: rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            animation: bubble-rise var(--duration) linear infinite;
            opacity: 0.7;
        }

        @keyframes bubble-rise {
            0% { 
                transform: translateY(var(--start-y)) translateX(var(--start-x));
                opacity: 0.7;
            }
            100% { 
                transform: translateY(calc(var(--start-y) - 200px)) translateX(calc(var(--start-x) + var(--drift)));
                opacity: 0;
            }
        }

        .sodium {
            position: absolute;
            top: -20px;
            left: 50%;
            width: 15px;
            height: 15px;
            background: white;
            border-radius: 50%;
            animation: drop-sodium 2s forwards;
            opacity: 0;
        }

        @keyframes drop-sodium {
            0% { transform: translateY(0) translateX(-50%); opacity: 1; }
            60% { transform: translateY(100px) translateX(-50%); opacity: 1; }
            61% { opacity: 0; }
            100% { transform: translateY(100px) translateX(-50%); opacity: 0; }
        }

        .explosion-flash {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: radial-gradient(circle, white, transparent);
            border-radius: 50%;
            opacity: 0;
            transform: translate(-50%, -50%);
            animation: flash 0.5s forwards;
        }

        @keyframes flash {
            0% { opacity: 0; width: 0; height: 0; }
            50% { opacity: 1; width: 200px; height: 200px; }
            100% { opacity: 0; width: 250px; height: 250px; }
        }

        .spark {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #ff4400;
            border-radius: 50%;
            opacity: 0;
            animation: spark-fly 0.8s linear forwards;
        }

        @keyframes spark-fly {
            0% { transform: translate(0, 0); opacity: 1; }
            100% { transform: translate(var(--end-x), var(--end-y)); opacity: 0; }
        }

        .ph-strip {
            position: absolute;
            width: 8px;
            height: 80px;
            background: #333;
            left: 50%;
            transform-origin: bottom center;
            animation: dip-strip 4s forwards;
        }

        .ph-strip.acid { animation-delay: 0s; }
        .ph-strip.neutral { animation-delay: 4s; }
        .ph-strip.base { animation-delay: 8s; }

        @keyframes dip-strip {
            0% { transform: translateX(-50%) translateY(-100%) rotate(0deg); background: #333; }
            25% { transform: translateX(-50%) translateY(50%) rotate(0deg); background: #333; }
            75% { transform: translateX(-50%) translateY(50%) rotate(0deg); background: var(--strip-color); }
            100% { transform: translateX(-50%) translateY(-100%) rotate(0deg); background: var(--strip-color); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="glowing-title">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    reaction_type = st.selectbox("Choose your reaction type:", 
                               ["", "Acid-Base (baking soda & vinegar)", 
                                "Exothermic (Warning: Explosive!)", 
                                "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid vinegar'></div>
                <div class='powder-stream'></div>
                <div class='bubbles'>
                    <div class='bubble' style='--duration: 2s; --start-y: 100px; --start-x: 20px; --drift: -10px;'></div>
                    <div class='bubble' style='--duration: 1.8s; --start-y: 90px; --start-x: 40px; --drift: 15px;'></div>
                    <div class='bubble' style='--duration: 2.2s; --start-y: 110px; --start-x: 60px; --drift: -5px;'></div>
                    <div class='bubble' style='--duration: 1.9s; --start-y: 95px; --start-x: 80px; --drift: 10px;'></div>
                    <div class='bubble' style='--duration: 2.1s; --start-y: 105px; --start-x: 30px; --drift: -15px;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding baking soda (NaHCO₃) to vinegar (CH₃COOH)...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid water'></div>
                <div class='sodium'></div>
                <div class='explosion-flash'></div>
                <div class='sparks'>
                    <div class='spark' style='--end-x: 50px; --end-y: -50px;'></div>
                    <div class='spark' style='--end-x: -30px; --end-y: -40px;'></div>
                    <div class='spark' style='--end-x: 20px; --end-y: -60px;'></div>
                    <div class='spark' style='--end-x: -40px; --end-y: -30px;'></div>
                    <div class='spark' style='--end-x: 35px; --end-y: -45px;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")

    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255,150,150,0.5);'>
                        <div class='ph-strip acid' style='--strip-color: #ff4444;'></div>
                    </div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(150,150,150,0.5);'>
                        <div class='ph-strip neutral' style='--strip-color: #44ff44;'></div>
                    </div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(150,150,255,0.5);'>
                        <div class='ph-strip base' style='--strip-color: #4444ff;'></div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Testing pH levels in different solutions...")
        st.write("Watch as the pH strips change color:")
        st.write("- Left beaker: Acidic solution (pH < 7) - Strip turns red")
        st.write("- Middle beaker: Neutral solution (pH = 7) - Strip turns green")
        st.write("- Right beaker: Basic solution (pH > 7) - Strip turns blue")

if __name__ == "__main__":
    lab()
