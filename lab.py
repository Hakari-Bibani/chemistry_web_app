import streamlit as st

def virtual_chemistry_lab():
    st.title("Virtual Chemistry Lab 🧪")

    # Choose a reaction to simulate
    reaction_choice = st.selectbox(
        "Choose a reaction:",
        ["Select", "Acid-Base (baking soda & vinegar)", "Exothermic Reaction", "Indicator Reaction"]
    )

    # Acid-Base Reaction: Baking Soda and Vinegar
    if reaction_choice == "Acid-Base (baking soda & vinegar)":
        st.header("Baking Soda and Vinegar Reaction")
        
        # Button to start the reaction
        if st.button("Start Reaction"):
            st.write("Initiating the Baking Soda and Vinegar Reaction...")

            # HTML and CSS for Beaker, Spoon, Baking Soda Pouring, and Fizzing Animation
            st.markdown("""
                <style>
                    .beaker {
                        position: relative;
                        width: 120px;
                        height: 200px;
                        background: rgba(255, 100, 100, 0.5); /* light red for vinegar */
                        border: 2px solid #aaa;
                        border-radius: 10px 10px 0 0;
                        overflow: hidden;
                    }

                    .liquid {
                        position: absolute;
                        bottom: 0;
                        width: 100%;
                        height: 50%; /* height of liquid in beaker */
                        background: rgba(255, 100, 100, 0.5);
                        animation: wave 1.5s ease-in-out infinite;
                    }

                    @keyframes wave {
                        0%, 100% { transform: translateX(0); }
                        50% { transform: translateX(5px); }
                    }

                    /* Spoon containing baking soda */
                    .spoon {
                        position: absolute;
                        top: -80px;
                        left: 50%;
                        transform: translateX(-50%);
                        width: 40px;
                        height: 20px;
                        background: #fff;
                        border-radius: 50% 50% 50% 0;
                        border: 2px solid #999;
                        animation: spoon-tilt 3s forwards;
                        transform-origin: bottom center;
                    }

                    /* Baking soda pouring animation */
                    .powder-stream {
                        position: absolute;
                        top: 20px;
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
                        100% { height: 80px; opacity: 1; }
                    }

                    /* Enhanced bubble animation for fizzing */
                    .bubble {
                        position: absolute;
                        background: rgba(200, 200, 200, 0.8);
                        border-radius: 50%;
                        animation: rise-fizz 1s infinite;
                    }

                    @keyframes rise-fizz {
                        0% { 
                            transform: translateY(0) translateX(var(--x-start));
                            opacity: 0.8;
                            width: var(--size);
                            height: var(--size);
                        }
                        100% { 
                            transform: translateY(-100px) translateX(var(--x-end));
                            opacity: 0;
                            width: calc(var(--size) * 2);
                            height: calc(var(--size) * 2);
                        }
                    }
                </style>
                
                <div class="beaker">
                    <div class="liquid"></div>
                    <div class="spoon"></div>
                    <div class="powder-stream"></div>
                    <div class="bubbles">
                        <div class="bubble" style="--x-start: 10px; --x-end: 20px; --size: 6px; animation-delay: 0s;"></div>
                        <div class="bubble" style="--x-start: -15px; --x-end: -10px; --size: 8px; animation-delay: 0.3s;"></div>
                        <div class="bubble" style="--x-start: 5px; --x-end: -5px; --size: 7px; animation-delay: 0.6s;"></div>
                        <div class="bubble" style="--x-start: -8px; --x-end: 15px; --size: 6px; animation-delay: 0.9s;"></div>
                        <div class="bubble" style="--x-start: 12px; --x-end: -12px; --size: 5px; animation-delay: 1.2s;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        else:
            st.write("Click 'Start Reaction' to see the fizzing effect of baking soda and vinegar!")

    # Additional sections for other reactions can go here (e.g., Exothermic Reaction, Indicator Reaction)
    # Example:
    elif reaction_choice == "Exothermic Reaction":
        st.header("Exothermic Reaction")
        st.write("This section can show the animation for an exothermic reaction.")
    
    elif reaction_choice == "Indicator Reaction":
        st.header("Indicator Reaction")
        st.write("This section can show the animation for an indicator reaction.")

# Run the virtual chemistry lab function
if __name__ == "__main__":
    virtual_chemistry_lab()
