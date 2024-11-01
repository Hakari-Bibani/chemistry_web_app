import streamlit as st

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
            background: rgba(255, 100, 100, 0.7); /* Light red liquid */
            transition: all 0.5s;
        }

        .spoon {
            position: absolute;
            top: -40px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 20px;
            background: #fff;
            border-radius: 50% 50% 0 0;
            overflow: hidden;
            box-shadow: 0 3px 5px rgba(0, 0, 0, 0.3);
            transition: transform 1s;
        }

        .baking-soda {
            position: absolute;
            top: 2px;
            left: 20%;
            width: 20px;
            height: 10px;
            background: #fff;
            border-radius: 50%;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
            opacity: 1;
            transition: opacity 1s, transform 1s;
        }

        .spoon.pour .baking-soda {
            opacity: 0;
            transform: translateY(100px);
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            animation: show-bubbles 3s forwards;
            animation-delay: 1s;
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

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 style="text-align: center; margin-bottom: 2em;">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        start_reaction = st.button("Add Baking Soda")

        # HTML for beaker and spoon animation
        if start_reaction:
            st.markdown("""
                <div class='beaker'>
                    <div class='liquid'></div>
                    <div class='spoon pour'>
                        <div class='baking-soda'></div>
                    </div>
                    <div class='bubbles'>
                        <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 10px; animation-delay: 0s;'></div>
                        <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 15px; animation-delay: 0.5s;'></div>
                        <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 12px; animation-delay: 1s;'></div>
                        <div class='bubble' style='--x-start: -8px; --x-end: 15px; --size: 8px; animation-delay: 1.5s;'></div>
                        <div class='bubble' style='--x-start: 12px; --x-end: -20px; --size: 14px; animation-delay: 2s;'></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("Step 1: Baking soda poured into vinegar...")
            st.write("Step 2: Observing the vigorous bubbling reaction...")
            st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

        else:
            st.markdown("""
                <div class='beaker'>
                    <div class='liquid'></div>
                    <div class='spoon'>
                        <div class='baking-soda'></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    lab()
