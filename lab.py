# Replace the existing Acid-Base reaction section in your lab.py with this updated version:

elif reaction_type == "Acid-Base (baking soda & vinegar)":
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
