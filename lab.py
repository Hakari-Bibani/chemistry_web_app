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
            background: rgba(255, 255, 255, 0.9);
            transition: all 1s;
        }

        .powder-container {
            position: absolute;
            top: -60px;
            left: 30%;
            width: 40px;
            height: 60px;
            background: #ddd;
            border: 2px solid #999;
            transform: rotate(0deg);
            transform-origin: bottom right;
            animation: tilt-pour 3s forwards;
        }

        @keyframes tilt-pour {
            0% { transform: rotate(0deg); }
            20% { transform: rotate(45deg); }
            80% { transform: rotate(45deg); }
            100% { transform: rotate(0deg); }
        }

        .powder-stream {
            position: absolute;
            bottom: -30px;
            right: 0;
            width: 8px;
            height: 0;
            background: white;
            animation: stream 3s forwards;
            clip-path: polygon(0 0, 100% 0, 80% 100%, 20% 100%);
        }

        @keyframes stream {
            0% { height: 0; opacity: 0; }
            20% { height: 40px; opacity: 1; }
            80% { height: 40px; opacity: 1; }
            100% { height: 0; opacity: 0; }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            animation: delay-show 3s forwards;
            opacity: 0;
        }

        @keyframes delay-show {
            0%, 90% { opacity: 0; }
            100% { opacity: 1; }
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 1.5s infinite;
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

        .explosion-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            animation: delay-explosion 3s forwards;
            opacity: 0;
        }

        @keyframes delay-explosion {
            0%, 90% { opacity: 0; }
            100% { opacity: 1; }
        }

        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100px;
            height: 100px;
            animation: explode 1.5s infinite;
        }

        @keyframes explode {
            0% { 
                transform: translate(-50%, -50%) scale(0.5);
                background: radial-gradient(circle, #ff4400 0%, transparent 70%);
                opacity: 1;
            }
            100% { 
                transform: translate(-50%, -50%) scale(2);
                background: radial-gradient(circle, #ff0000 0%, transparent 70%);
                opacity: 0;
            }
        }

        .fire {
            position: absolute;
            bottom: 50%;
            left: 50%;
            width: 40px;
            height: 60px;
            background: linear-gradient(to top, #ff4400, #ff8800);
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            animation: flicker 0.5s infinite alternate;
            transform-origin: center bottom;
        }

        @keyframes flicker {
            0% { transform: translate(-50%, 0) scale(1, 1); }
            100% { transform: translate(-50%, 0) scale(1.2, 1.1); }
        }

        .ph-strip-container {
            position: absolute;
            top: -100px;
            left: 50%;
            transform: translateX(-50%);
            width: 15px;
            height: 100px;
            animation: dip-sequence 6s forwards;
        }

        .ph-strip {
            width: 100%;
            height: 100%;
            background: white;
            transition: background-color 1s;
        }

        @keyframes dip-sequence {
            0% { transform: translate(-50%, 0); }
            20% { transform: translate(-50%, 150px); }
            40% { transform: translate(-50%, 150px); }
            60% { transform: translate(-50%, 0); }
            100% { transform: translate(-50%, 0); }
        }

        .ph-strip.acid { animation: color-change-acid 6s forwards; }
        .ph-strip.neutral { animation: color-change-neutral 6s forwards; }
        .ph-strip.base { animation: color-change-base 6s forwards; }

        @keyframes color-change-acid {
            0%, 50% { background: white; }
            100% { background: #ff6b6b; }
        }

        @keyframes color-change-neutral {
            0%, 50% { background: white; }
            100% { background: #51cf66; }
        }

        @keyframes color-change-base {
            0%, 50% { background: white; }
            100% { background: #339af0; }
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
                <div class='liquid'></div>
                <div class='powder-container'>
                    <div class='powder-stream'></div>
                </div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 8px; left: 20%; animation-delay: 3.2s;'></div>
                    <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 12px; left: 40%; animation-delay: 3.4s;'></div>
                    <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 10px; left: 60%; animation-delay: 3.6s;'></div>
                    <div class='bubble' style='--x-start: -8px; --x-end: 15px; --size: 9px; left: 80%; animation-delay: 3.8s;'></div>
                    <div class='bubble' style='--x-start: 12px; --x-end: -20px; --size: 11px; left: 30%; animation-delay: 4.0s;'></div>
                    <div class='bubble' style='--x-start: -10px; --x-end: 25px; --size: 10px; left: 70%; animation-delay: 4.2s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding baking soda (NaHCO₃) to vinegar (CH₃COOH)...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid'></div>
                <div class='powder-container'>
                    <div class='powder-stream'></div>
                </div>
                <div class='explosion-container'>
                    <div class='explosion'></div>
                    <div class='fire'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")
        
    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker' style='margin: 0 40px;'>
                    <div class='liquid'></div>
                    <div class='ph-strip-container'>
                        <div class='ph-strip acid'></div>
                    </div>
                </div>
                <div class='beaker' style='margin: 0 40px;'>
                    <div class='liquid'></div>
                    <div class='ph-strip-container'>
                        <div class='ph-strip neutral'></div>
                    </div>
                </div>
                <div class='beaker' style='margin: 0 40px;'>
                    <div class='liquid'></div>
                    <div class='ph-strip-container'>
                        <div class='ph-strip base'></div>
                    </div>
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
