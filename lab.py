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
            width: 120px;
            height: 180px;
            border: 4px solid #999;
            border-radius: 0 0 20px 20px;
            position: relative;
            margin: 20px;
            background: transparent;
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
            background: rgba(255, 255, 255, 0.8);
            transition: all 1s;
        }

        .powder-stream {
            position: absolute;
            top: -50px;
            left: 50%;
            width: 8px;
            height: 0;
            background: white;
            transform-origin: top center;
            animation: pour 3s forwards;
            clip-path: polygon(0 0, 100% 0, 80% 100%, 20% 100%);
        }

        @keyframes pour {
            0% { height: 0; opacity: 0; }
            10% { height: 100px; opacity: 1; }
            90% { height: 100px; opacity: 1; }
            100% { height: 0; opacity: 0; }
        }

        .powder-particles {
            position: absolute;
            pointer-events: none;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: white;
            border-radius: 50%;
            animation: fall-scatter 2s linear forwards;
        }

        @keyframes fall-scatter {
            0% { transform: translate(0, 0); opacity: 1; }
            100% { transform: translate(var(--x-end), var(--y-end)); opacity: 0; }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            pointer-events: none;
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 2s infinite;
            opacity: 0;
        }

        @keyframes rise {
            0% { 
                transform: translateY(0) translateX(var(--x-start));
                opacity: 0.8;
                width: var(--size);
                height: var(--size);
            }
            100% { 
                transform: translateY(-100px) translateX(var(--x-end));
                opacity: 0;
                width: calc(var(--size) * 1.5);
                height: calc(var(--size) * 1.5);
            }
        }

        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0);
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, #ff4400 0%, transparent 70%);
            animation: explode 1.5s forwards;
            opacity: 0;
        }

        @keyframes explode {
            0% { 
                transform: translate(-50%, -50%) scale(0);
                opacity: 0;
            }
            50% { 
                transform: translate(-50%, -50%) scale(2);
                opacity: 1;
            }
            100% { 
                transform: translate(-50%, -50%) scale(3);
                opacity: 0;
            }
        }

        .ph-strip {
            position: absolute;
            width: 10px;
            height: 80px;
            background: #fff;
            left: 50%;
            transform-origin: bottom center;
            animation: dip 6s forwards;
        }

        .ph-strip.acid { animation: dip-acid 6s forwards; }
        .ph-strip.neutral { animation: dip-neutral 6s forwards; }
        .ph-strip.base { animation: dip-base 6s forwards; }

        @keyframes dip-acid {
            0% { transform: translateX(-50%) translateY(-100%); background: #fff; }
            25% { transform: translateX(-50%) translateY(30%); background: #fff; }
            75% { transform: translateX(-50%) translateY(30%); background: #ff6b6b; }
            100% { transform: translateX(-50%) translateY(-100%); background: #ff6b6b; }
        }

        @keyframes dip-neutral {
            0% { transform: translateX(-50%) translateY(-100%); background: #fff; }
            25% { transform: translateX(-50%) translateY(30%); background: #fff; }
            75% { transform: translateX(-50%) translateY(30%); background: #51cf66; }
            100% { transform: translateX(-50%) translateY(-100%); background: #51cf66; }
        }

        @keyframes dip-base {
            0% { transform: translateX(-50%) translateY(-100%); background: #fff; }
            25% { transform: translateX(-50%) translateY(30%); background: #fff; }
            75% { transform: translateX(-50%) translateY(30%); background: #339af0; }
            100% { transform: translateX(-50%) translateY(-100%); background: #339af0; }
        }

        .sparks {
            position: absolute;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }

        .spark {
            position: absolute;
            width: 6px;
            height: 6px;
            background: #ff4400;
            border-radius: 50%;
            filter: blur(2px);
            animation: spark 1s linear forwards;
        }

        @keyframes spark {
            0% { transform: translate(0, 0) scale(1); opacity: 1; }
            100% { 
                transform: translate(var(--x-end), var(--y-end)) scale(0);
                opacity: 0;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="glowing-title">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,255,255,0.8);'></div>
                <div class='powder-stream'></div>
                <div class='powder-particles'>
                    <div class='particle' style='--x-end: 5px; --y-end: 100px; animation-delay: 0.2s;'></div>
                    <div class='particle' style='--x-end: -8px; --y-end: 120px; animation-delay: 0.4s;'></div>
                    <div class='particle' style='--x-end: 12px; --y-end: 90px; animation-delay: 0.6s;'></div>
                </div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 8px; animation-delay: 1s;'></div>
                    <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 12px; animation-delay: 1.5s;'></div>
                    <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 10px; animation-delay: 2s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding baking soda (NaHCO₃) to vinegar (CH₃COOH)...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,255,255,0.9);'></div>
                <div class='powder-stream'></div>
                <div class='explosion'></div>
                <div class='sparks'>
                    <div class='spark' style='--x-end: 100px; --y-end: -80px; animation-delay: 2s;'></div>
                    <div class='spark' style='--x-end: -80px; --y-end: -60px; animation-delay: 2.2s;'></div>
                    <div class='spark' style='--x-end: 60px; --y-end: -100px; animation-delay: 2.4s;'></div>
                    <div class='spark' style='--x-end: -100px; --y-end: -90px; animation-delay: 2.6s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")
        
    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker' style='margin: 0 40px;'>
                    <div class='liquid' style='background: rgba(255,200,200,0.3);'></div>
                    <div class='ph-strip acid'></div>
                </div>
                <div class='beaker' style='margin: 0 40px;'>
                    <div class='liquid' style='background: rgba(200,255,200,0.3);'></div>
                    <div class='ph-strip neutral'></div>
                </div>
                <div class='beaker' style='margin: 0 40px;'>
                    <div class='liquid' style='background: rgba(200,200,255,0.3);'></div>
                    <div class='ph-strip base'></div>
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
