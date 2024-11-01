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
            <div class='liquid' style='background: rgba(255, 200, 200, 0.9); /* Light red for vinegar */'>
                <!-- Add subtle liquid movement animation -->
                <div class='liquid-movement'></div>
            </div>
            <div class='spoon-container'>
                <div class='spoon'>
                    <div class='powder-heap'></div>
                </div>
            </div>
            <div class='powder-stream' style='display: none;'></div>
            <div class='bubbles'>
                <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 8px; animation-delay: 0s; background: rgba(200, 200, 200, 0.8);'></div>
                <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 12px; animation-delay: 0.3s; background: rgba(200, 200, 200, 0.8);'></div>
                <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 10px; animation-delay: 0.6s; background: rgba(200, 200, 200, 0.8);'></div>
                <div class='bubble' style='--x-start: -8px; --x-end: 15px; --size: 6px; animation-delay: 0.9s; background: rgba(200, 200, 200, 0.8);'></div>
                <div class='bubble' style='--x-start: 12px; --x-end: -20px; --size: 9px; animation-delay: 1.2s; background: rgba(200, 200, 200, 0.8);'></div>
            </div>
        </div>
        <button class='pour-button'>Pour Baking Soda</button>
    """, unsafe_allow_html=True)
    
    # Add these new CSS rules to your existing style section:
    st.markdown("""
        <style>
        /* Add these new styles to your existing CSS */
        .liquid-movement {
            position: absolute;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, transparent 45%, rgba(255, 255, 255, 0.1) 50%, transparent 55%);
            animation: move-liquid 3s infinite linear;
        }

        @keyframes move-liquid {
            0% { transform: translateX(-50%) }
            100% { transform: translateX(50%) }
        }

        .spoon-container {
            position: absolute;
            top: -60px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 20px;
            transition: transform 0.5s;
        }

        .spoon {
            position: relative;
            width: 100%;
            height: 100%;
            background: #ddd;
            border-radius: 50% 50% 0 0;
            transform: rotate(-5deg);
        }

        .spoon::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 8px;
            height: 40px;
            background: #ddd;
            transform: translate(-50%, 0);
        }

        .powder-heap {
            position: absolute;
            top: -5px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 15px;
            background: white;
            border-radius: 50%;
        }

        .pour-button {
            display: block;
            margin: 20px auto;
            padding: 10px 20px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }

        .pour-button:hover {
            background: #45a049;
        }

        /* Update existing bubble animation */
        .bubble {
            box-shadow: inset 1px 1px 1px rgba(255, 255, 255, 0.4);
        }

        @keyframes rise {
            0% { 
                transform: translateY(0) translateX(var(--x-start)) scale(1);
                opacity: 0.8;
            }
            50% {
                transform: translateY(-60px) translateX(calc(var(--x-end) * 0.5)) scale(1.2);
                opacity: 0.6;
            }
            100% { 
                transform: translateY(-120px) translateX(var(--x-end)) scale(0.8);
                opacity: 0;
            }
        }
        </style>

        <script>
            const pourButton = document.querySelector('.pour-button');
            const spoonContainer = document.querySelector('.spoon-container');
            const powderStream = document.querySelector('.powder-stream');
            
            pourButton.addEventListener('click', () => {
                spoonContainer.style.transform = 'translateX(-50%) rotate(45deg)';
                powderStream.style.display = 'block';
                setTimeout(() => {
                    spoonContainer.style.transform = 'translateX(-50%) rotate(-5deg)';
                    powderStream.style.display = 'none';
                }, 3000);
            });
        </script>
    """, unsafe_allow_html=True)
    
    st.write("Step 1: Click the button to add baking soda to vinegar solution...")
    st.write("Step 2: Watch the vigorous fizzing reaction!")
    st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")
        
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
