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
            transform-style: preserve-3d;
            perspective: 1000px;
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
            transition: all 0.5s;
            transform-origin: bottom;
        }

        .powder-container {
            position: absolute;
            top: -60px;
            left: 50%;
            transform: translateX(-50%) rotate(15deg);
            width: 40px;
            height: 60px;
            animation: tilt-pour 3s forwards;
        }

        @keyframes tilt-pour {
            0% { transform: translateX(-50%) rotate(0deg); }
            20% { transform: translateX(-50%) rotate(15deg); }
            80% { transform: translateX(-50%) rotate(15deg); }
            100% { transform: translateX(-50%) rotate(0deg); }
        }

        .powder-stream {
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 6px;
            height: 0;
            background: white;
            transform-origin: top;
            animation: pour-powder 3s forwards;
            filter: blur(1px);
        }

        @keyframes pour-powder {
            0% { height: 0; opacity: 0; }
            20% { height: 60px; opacity: 0.8; }
            80% { height: 60px; opacity: 0.8; }
            100% { height: 0; opacity: 0; }
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 50%;
            opacity: 0;
            animation: bubble-rise 2s ease-out forwards;
        }

        @keyframes bubble-rise {
            0% {
                transform: translate(var(--x-start), 0) scale(0.5);
                opacity: 0.8;
            }
            100% {
                transform: translate(var(--x-end), -150px) scale(1.5);
                opacity: 0;
            }
        }

        .explosion-container {
            position: absolute;
            width: 100%;
            height: 100%;
            perspective: 1000px;
        }

        .explosion {
            position: absolute;
            top: 25%;
            left: 0;
            width: 100%;
            height: 75%;
            transform-origin: center;
            animation: explode-fire 2s forwards;
            opacity: 0;
        }

        @keyframes explode-fire {
            0% { 
                transform: scale(0.5);
                opacity: 0;
                background: radial-gradient(circle, #ff4400 0%, #ff0000 40%, transparent 70%);
            }
            50% { 
                transform: scale(1.5);
                opacity: 1;
                background: radial-gradient(circle, #ff4400 20%, #ff0000 60%, transparent 90%);
            }
            100% { 
                transform: scale(2);
                opacity: 0;
                background: radial-gradient(circle, #ff4400 40%, #ff0000 80%, transparent 100%);
            }
        }

        .spark {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #ff6600;
            border-radius: 50%;
            filter: blur(1px);
            animation: spark-fly 1s ease-out forwards;
        }

        @keyframes spark-fly {
            0% { 
                transform: translate(0, 0) scale(1);
                opacity: 1;
            }
            100% { 
                transform: translate(var(--x-end), var(--y-end)) scale(0);
                opacity: 0;
            }
        }

        .ph-strip {
            position: absolute;
            width: 8px;
            height: 70px;
            background: #333;
            left: 50%;
            transform-origin: top center;
            animation: dip-strip 4s forwards;
        }

        @keyframes dip-strip {
            0% { transform: translateX(-50%) translateY(-100%) rotate(0deg); }
            20% { transform: translateX(-50%) translateY(30%) rotate(0deg); }
            80% { transform: translateX(-50%) translateY(30%) rotate(0deg); }
            100% { transform: translateX(-50%) translateY(-100%) rotate(0deg); }
        }

        .ph-strip.acid { animation: dip-strip-acid 4s forwards; }
        .ph-strip.neutral { animation: dip-strip-neutral 4s forwards; }
        .ph-strip.base { animation: dip-strip-base 4s forwards; }

        @keyframes dip-strip-acid {
            0% { transform: translateX(-50%) translateY(-100%); background: #333; }
            20% { transform: translateX(-50%) translateY(30%); background: #333; }
            80% { transform: translateX(-50%) translateY(30%); background: #ff6b6b; }
            100% { transform: translateX(-50%) translateY(-100%); background: #ff6b6b; }
        }

        @keyframes dip-strip-neutral {
            0% { transform: translateX(-50%) translateY(-100%); background: #333; }
            20% { transform: translateX(-50%) translateY(30%); background: #333; }
            80% { transform: translateX(-50%) translateY(30%); background: #51cf66; }
            100% { transform: translateX(-50%) translateY(-100%); background: #51cf66; }
        }

        @keyframes dip-strip-base {
            0% { transform: translateX(-50%) translateY(-100%); background: #333; }
            20% { transform: translateX(-50%) translateY(30%); background: #333; }
            80% { transform: translateX(-50%) translateY(30%); background: #339af0; }
            100% { transform: translateX(-50%) translateY(-100%); background: #339af0; }
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
                <div id='bubbles'></div>
                <script>
                    function createBubbles() {
                        const bubbles = document.getElementById('bubbles');
                        for(let i = 0; i < 20; i++) {
                            const bubble = document.createElement('div');
                            bubble.className = 'bubble';
                            bubble.style.setProperty('--x-start', `${Math.random() * 100 - 50}px`);
                            bubble.style.setProperty('--x-end', `${Math.random() * 100 - 50}px`);
                            bubble.style.left = `${Math.random() * 80 + 10}%`;
                            bubble.style.animationDelay = `${i * 0.1 + 1}s`;
                            bubble.style.width = `${Math.random() * 8 + 4}px`;
                            bubble.style.height = bubble.style.width;
                            bubbles.appendChild(bubble);
                        }
                    }
                    createBubbles();
                </script>
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
                </div>
                <div id='sparks'></div>
                <script>
                    function createSparks() {
                        const sparks = document.getElementById('sparks');
                        for(let i = 0; i < 15; i++) {
                            const spark = document.createElement('div');
                            spark.className = 'spark';
                            spark.style.setProperty('--x-end', `${Math.random() * 200 - 100}px`);
                            spark.style.setProperty('--y-end', `${-Math.random() * 100 - 50}px`);
                            spark.style.left = '50%';
                            spark.style.top = '50%';
                            spark.style.animationDelay = `${i * 0.1 + 2}s`;
                            sparks.appendChild(spark);
                        }
                    }
                    createSparks();
                </script>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")
        
    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker'>
                    <div class='liquid'></div>
                    <div class='ph-strip acid'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid'></div>
                    <div class='ph-strip neutral'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid'></div>
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
