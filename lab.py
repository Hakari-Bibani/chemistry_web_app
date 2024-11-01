import streamlit as st
import time

def lab():
    # Enhanced CSS with more realistic animations and liquid motion
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
            width: 150px;
            height: 200px;
            border: 4px solid #999;
            border-radius: 0 0 20px 20px;
            position: relative;
            margin: 20px;
            background: linear-gradient(to bottom, #ffffff00, #ffffff40);
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
            background: rgba(255, 255, 255, 0.8);
            transition: all 2s;
            animation: liquid-motion 3s infinite ease-in-out;
        }

        @keyframes liquid-motion {
            0%, 100% { transform: translateX(-2px) rotate(-1deg); }
            50% { transform: translateX(2px) rotate(1deg); }
        }

        .powder-stream {
            position: absolute;
            top: -20px;
            left: 50%;
            width: 4px;
            height: 0;
            background: white;
            opacity: 0;
            transform-origin: top;
            animation: pour-powder 3s forwards;
        }

        @keyframes pour-powder {
            0% { height: 0; opacity: 0; }
            10% { height: 100px; opacity: 1; }
            90% { height: 100px; opacity: 1; }
            100% { height: 0; opacity: 0; }
        }

        .powder-particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .particle {
            position: absolute;
            width: 3px;
            height: 3px;
            background: white;
            border-radius: 50%;
            animation: fall-particle 2s forwards;
        }

        @keyframes fall-particle {
            0% { transform: translate(0, -50px); opacity: 1; }
            100% { transform: translate(var(--x-end), 150px); opacity: 0; }
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
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise-bubble 1.5s infinite;
        }

        @keyframes rise-bubble {
            0% { 
                transform: translate(var(--x-start), 100%) scale(0.3);
                opacity: 0.8;
            }
            100% { 
                transform: translate(var(--x-end), -100%) scale(1);
                opacity: 0;
            }
        }

        .sodium-piece {
            position: absolute;
            top: -30px;
            left: 50%;
            width: 15px;
            height: 15px;
            background: linear-gradient(135deg, #fff, #ddd);
            border-radius: 3px;
            transform: translateX(-50%);
            animation: drop-sodium 1s forwards;
        }

        @keyframes drop-sodium {
            0% { transform: translateX(-50%) translateY(0) rotate(0deg); }
            100% { transform: translateX(-50%) translateY(200px) rotate(720deg); }
        }

        .explosion-effect {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: radial-gradient(circle, #ff4400 0%, transparent 70%);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            opacity: 0;
            pointer-events: none;
        }

        .explosion-effect.active {
            animation: explode-effect 0.5s forwards;
        }

        @keyframes explode-effect {
            0% { 
                width: 0;
                height: 0;
                opacity: 1;
            }
            100% { 
                width: 300px;
                height: 300px;
                opacity: 0;
            }
        }

        .spark {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #ff4400;
            border-radius: 50%;
            filter: blur(1px);
            animation: spark-fly 0.6s linear forwards;
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
            height: 60px;
            background: #333;
            left: 50%;
            transform-origin: bottom center;
            animation: dip-strip 4s forwards;
        }

        .ph-strip.acid { animation: dip-strip-acid 4s forwards; }
        .ph-strip.neutral { animation: dip-strip-neutral 4s forwards; }
        .ph-strip.base { animation: dip-strip-base 4s forwards; }

        @keyframes dip-strip-acid {
            0% { transform: translateX(-50%) translateY(-100%); background: #333; }
            25% { transform: translateX(-50%) translateY(50%); background: #333; }
            75% { transform: translateX(-50%) translateY(50%); background: #ff4444; }
            100% { transform: translateX(-50%) translateY(-100%); background: #ff4444; }
        }

        @keyframes dip-strip-neutral {
            0% { transform: translateX(-50%) translateY(-100%); background: #333; }
            25% { transform: translateX(-50%) translateY(50%); background: #333; }
            75% { transform: translateX(-50%) translateY(50%); background: #44ff44; }
            100% { transform: translateX(-50%) translateY(-100%); background: #44ff44; }
        }

        @keyframes dip-strip-base {
            0% { transform: translateX(-50%) translateY(-100%); background: #333; }
            25% { transform: translateX(-50%) translateY(50%); background: #333; }
            75% { transform: translateX(-50%) translateY(50%); background: #4444ff; }
            100% { transform: translateX(-50%) translateY(-100%); background: #4444ff; }
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
                <div class='liquid' style='background: rgba(255,255,255,0.8);'>
                    <div class='powder-stream'></div>
                    <div class='powder-particles'></div>
                </div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-start: 10px; --x-end: 20px; animation-delay: 0s; width: 10px; height: 10px;'></div>
                    <div class='bubble' style='--x-start: -15px; --x-end: -25px; animation-delay: 0.3s; width: 8px; height: 8px;'></div>
                    <div class='bubble' style='--x-start: 5px; --x-end: -10px; animation-delay: 0.6s; width: 12px; height: 12px;'></div>
                    <div class='bubble' style='--x-start: -10px; --x-end: 15px; animation-delay: 0.9s; width: 9px; height: 9px;'></div>
                </div>
            </div>
            <script>
                function createParticles() {
                    const particles = document.querySelector('.powder-particles');
                    for (let i = 0; i < 20; i++) {
                        const particle = document.createElement('div');
                        particle.className = 'particle';
                        particle.style.setProperty('--x-end', (Math.random() * 40 - 20) + 'px');
                        particle.style.animationDelay = (Math.random() * 2) + 's';
                        particles.appendChild(particle);
                    }
                }
                createParticles();
            </script>
        """, unsafe_allow_html=True)
        
        st.write("Baking soda (NaHCO₃) is being added to vinegar (CH₃COOH)...")
        st.write("Watch the vigorous reaction as CO₂ is produced!")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,255,255,0.9);'></div>
                <div class='sodium-piece'></div>
                <div class='explosion-effect'></div>
                <div class='sparks'>
                    <div class='spark' style='--x-end: 50px; --y-end: -50px; animation-delay: 1s;'></div>
                    <div class='spark' style='--x-end: -30px; --y-end: -40px; animation-delay: 1.2s;'></div>
                    <div class='spark' style='--x-end: 20px; --y-end: -60px; animation-delay: 1.4s;'></div>
                    <div class='spark' style='--x-end: -40px; --y-end: -30px; animation-delay: 1.6s;'></div>
                </div>
            </div>
            <script>
                setTimeout(() => {
                    document.querySelector('.explosion-effect').classList.add('active');
                }, 1000);
            </script>
        """, unsafe_allow_html=True)
        
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("Watch the explosive reaction!")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")

    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255,192,192,0.4);'></div>
                    <div class='ph-strip acid'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(192,192,192,0.4);'></div>
                    <div class='ph-strip neutral'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(192,192,255,0.4);'></div>
                    <div class='ph-strip base'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Testing pH levels in different solutions...")
        st.write("Observe the color changes:")
        st.write("- Red: Acidic (pH < 7)")
        st.write("- Green: Neutral (pH = 7)")
        st.write("- Blue: Basic (pH > 7)")

if __name__ == "__main__":
    lab()
