import streamlit as st
import time

def lab():
    # Add this new JavaScript to handle the animation
    st.markdown("""
        <script>
            function initializeReaction() {
                const pourButton = document.querySelector('.pour-button');
                const spoonContainer = document.querySelector('.spoon-container');
                const powderStream = document.querySelector('.powder-stream');
                
                if (pourButton) {
                    pourButton.addEventListener('click', () => {
                        if (spoonContainer) {
                            spoonContainer.style.transform = 'translateX(-50%) rotate(45deg)';
                        }
                        if (powderStream) {
                            powderStream.style.display = 'block';
                        }
                        setTimeout(() => {
                            if (spoonContainer) {
                                spoonContainer.style.transform = 'translateX(-50%) rotate(-5deg)';
                            }
                            if (powderStream) {
                                powderStream.style.display = 'none';
                            }
                        }, 3000);
                    });
                }
            }
            
            // Run after DOM is loaded
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', initializeReaction);
            } else {
                initializeReaction();
            }
        </script>
    """, unsafe_allow_html=True)

    # Your existing styles
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
            background: rgba(255, 200, 200, 0.9);  /* Light red vinegar color */
            transition: all 0.5s;
        }

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
            z-index: 100;
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

        .powder-stream {
            position: absolute;
            top: 40px;
            left: 50%;
            width: 6px;
            height: 80px;
            background: rgba(255, 255, 255, 0.9);
            filter: blur(1px);
            transform-origin: top center;
            display: none;
            z-index: 99;
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
            background: rgba(200, 200, 200, 0.8);
            border-radius: 50%;
            animation: rise 1.5s infinite;
            box-shadow: inset 1px 1px 1px rgba(255, 255, 255, 0.4);
            width: var(--size);
            height: var(--size);
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
            font-family: sans-serif;
            font-size: 16px;
        }

        .pour-button:hover {
            background: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 style="text-align: center; margin-bottom: 2em;">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown("""
                <div class='beaker'>
                    <div class='liquid'>
                        <div class='liquid-movement'></div>
                    </div>
                    <div class='spoon-container'>
                        <div class='spoon'>
                            <div class='powder-heap'></div>
                        </div>
                    </div>
                    <div class='powder-stream'></div>
                    <div class='bubbles'>
                        <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 8px; animation-delay: 0s;'></div>
                        <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 12px; animation-delay: 0.3s;'></div>
                        <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 10px; animation-delay: 0.6s;'></div>
                        <div class='bubble' style='--x-start: -8px; --x-end: 15px; --size: 6px; animation-delay: 0.9s;'></div>
                        <div class='bubble' style='--x-start: 12px; --x-end: -20px; --size: 9px; animation-delay: 1.2s;'></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("Pour Baking Soda"):
                st.markdown("""
                    <script>
                        const spoonContainer = document.querySelector('.spoon-container');
                        const powderStream = document.querySelector('.powder-stream');
                        
                        if (spoonContainer && powderStream) {
                            spoonContainer.style.transform = 'translateX(-50%) rotate(45deg)';
                            powderStream.style.display = 'block';
                            
                            setTimeout(() => {
                                spoonContainer.style.transform = 'translateX(-50%) rotate(-5deg)';
                                powderStream.style.display = 'none';
                            }, 3000);
                        }
                    </script>
                """, unsafe_allow_html=True)

        st.write("Step 1: Click the button to add baking soda to vinegar solution...")
        st.write("Step 2: Watch the vigorous fizzing reaction!")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    # [Rest of your code for other reactions remains the same]

if __name__ == "__main__":
    lab()
