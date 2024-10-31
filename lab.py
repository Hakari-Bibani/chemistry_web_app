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

        .beaker::before {
            content: '';
            position: absolute;
            top: -12px;
            left: -15px;
            right: -15px;
            height: 25px;
            background: #ddd;
            border-radius: 5px;
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

        @keyframes tilt-pour {
            0% { transform: translateX(-50%) rotate(-5deg); }
            20% { transform: translateX(-50%) rotate(45deg); }
            80% { transform: translateX(-50%) rotate(45deg); }
            100% { transform: translateX(-50%) rotate(-5deg); }
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
                transform: translateY(-120px) translateX(var(--x-end));
                opacity: 0;
                width: calc(var(--size) * 2);
                height: calc(var(--size) * 2);
            }
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
            animation-delay: 3s;
            pointer-events: none;
        }

        @keyframes explode {
            0% { 
                transform: translate(-50%, -50%) scale(0);
                opacity: 0;
                background: radial-gradient(circle, #ff4400 0%, transparent 70%);
            }
            50% { 
                transform: translate(-50%, -50%) scale(2);
                opacity: 1;
                background: radial-gradient(circle, #ff8800 0%, #ff4400 30%, transparent 70%);
            }
            100% { 
                transform: translate(-50%, -50%) scale(3);
                opacity: 0;
                background: radial-gradient(circle, #ffbb00 0%, #ff8800 30%, transparent 70%);
            }
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

        @keyframes burn {
            0%, 100% { 
                transform: scaleY(1);
                opacity: 0.8;
                background: linear-gradient(to top, #ff4400, #ff8800, transparent);
            }
            50% { 
                transform: scaleY(1.2);
                opacity: 1;
                background: linear-gradient(to top, #ff8800, #ffbb00, transparent);
            }
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

        @keyframes spark {
            0% { transform: translate(0, 0); opacity: 1; }
            100% { 
                transform: translate(var(--x-end), var(--y-end));
                opacity: 0;
            }
        }

        .ph-strip {
            position: absolute;
            width: 12px;
            height: 100px;
            background: #333;
            left: 50%;
            transform-origin: bottom center;
            animation: dip 6s forwards;
        }

        .ph-strip.acid { animation: dip-acid 6s forwards; }
        .ph-strip.neutral { animation: dip-neutral 6s forwards; }
        .ph-strip.base { animation: dip-base 6s forwards; }

        @keyframes dip-acid {
            0% { transform: translateX(-50%) translateY(-120%) rotate(0deg); background: #333; }
            20% { transform: translateX(-50%) translateY(30%) rotate(0deg); background: #333; }
            80% { transform: translateX(-50%) translateY(30%) rotate(0deg); background: #ff6b6b; }
            100% { transform: translateX(-50%) translateY(-120%) rotate(0deg); background: #ff6b6b; }
        }

        @keyframes dip-neutral {
            0% { transform: translateX(-50%) translateY(-120%) rotate(0deg); background: #333; }
            20% { transform: translateX(-50%) translateY(30%) rotate(0deg); background: #333; }
            80% { transform: translateX(-50%) translateY(30%) rotate(0deg); background: #51cf66; }
            100% { transform: translateX(-50%) translateY(-120%) rotate(0deg); background: #51cf66; }
        }

        @keyframes dip-base {
            0% { transform: translateX(-50%) translateY(-120%) rotate(0deg); background: #333; }
            20% { transform: translateX(-50%) translateY(30%) rotate(0deg); background: #333; }
            80% { transform: translateX(-50%) translateY(30%) rotate(0deg); background: #339af0; }
            100% { transform: translateX(-50%) translateY(-120%) rotate(0deg); background: #339af0; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 style="text-align: center; margin-bottom: 2em;">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,255,255,0.9);'></div>
                <div class='powder-container'></div>
                <div class='powder-stream'></div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 10px; animation-delay: 0s;'></div>
                    <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 15px; animation-delay: 0.5s;'></div>
                    <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 12px; animation-delay: 1s;'></div>
                    <div class='bubble' style='--x-start: -8px; --x-end: 15px; --size: 8px; animation-delay: 1.5s;'></div>
                    <div class='bubble' style='--x-start: 12px; --x-end: -20px; --size: 14px; animation-delay: 2s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Slowly adding baking soda to vinegar solution...")
        st.write("Step 2: Observing the vigorous bubble formation...")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,255,255,0.9);'></div>
                <div class='powder-container'></div>
                <div class='powder-stream'></div>
                <div class='explosion'></div>
                <div class='fire'></div>
                <div class='sparks'>
                    <div class='spark' style='--x-end: 120px; --y-end: -100px; animation-delay: 3.2s;'></div>
                    <div class='spark' style='--x-end: -100px; --y-end: -80px; animation-delay: 3.4s;'></div>
                    <div class='spark' style='--x-end: 80px; --y-end: -120px; animation-delay: 3.6s;'></div>
                    <div class='spark' style='--x-end: -120px; --y-end: -90px; animation-delay: 3.8s;'></div>
                    <div class='spark' style='--x-end: 100px; --y-end: -110px; animation-delay: 4.0s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Carefully adding sodium to water...")
        st.write("Step 2: Observing the violent reaction...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) + Energy")
        
    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255,255,255,0.95);'></div>
                    <div class='ph-strip acid'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255,255,255,0.95);'></div>
                    <div class='ph-strip neutral'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255,255,255,0.95);'></div>
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
