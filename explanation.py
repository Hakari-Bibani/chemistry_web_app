import streamlit as st

# Add the glowing title
st.markdown('<h1 class="glowing-title-explanation">📚 Chemistry Concepts & Explanations</h1>', unsafe_allow_html=True)

# Create styled cards for options
st.markdown("""
<div class="option-cards">
    <div class="card" onclick="toggleDetail('phDetail')">pH</div>
    <div class="card" onclick="toggleDetail('pohDetail')">pOH</div>
    <div class="card" onclick="toggleDetail('molarityDetail')">Molarity</div>
</div>
<div id="phDetail" class="detail" style="display:none;">
    <h2>Understanding pH</h2>
    <p>What is pH? pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.</p>
    <h3>Test Your Knowledge! 📝</h3>
    <p>What pH value represents a neutral solution?</p>
    <button onclick="showAnswer('phAnswer')">Show Answers</button>
    <p id="phAnswer" style="display:none;">Correct Answer: 7</p>
</div>
<div id="pohDetail" class="detail" style="display:none;">
    <h2>Understanding pOH</h2>
    <p>What is pOH? pOH is a measure of the hydroxide ion concentration in a solution.</p>
    <h3>Test Your Knowledge! 📝</h3>
    <p>What pOH value represents a neutral solution?</p>
    <button onclick="showAnswer('pohAnswer')">Show Answers</button>
    <p id="pohAnswer" style="display:none;">Correct Answer: 7</p>
</div>
<div id="molarityDetail" class="detail" style="display:none;">
    <h2>Understanding Molarity</h2>
    <p>Molarity (M) is a measure of the concentration of a solution, expressed as the number of moles of solute per liter of solution.</p>
    <h3>Test Your Knowledge! 📝</h3>
    <p>If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?</p>
    <button onclick="showAnswer('molarityAnswer')">Show Answers</button>
    <p id="molarityAnswer" style="display:none;">Correct Answer: 4</p>
</div>
""", unsafe_allow_html=True)

# Add JavaScript to toggle details
st.markdown("""
<script>
    function toggleDetail(detailId) {
        var details = document.querySelectorAll('.detail');
        details.forEach(function(detail) {
            if (detail.id === detailId) {
                detail.style.display = detail.style.display === 'none' ? 'block' : 'none';
            } else {
                detail.style.display = 'none';
            }
        });
    }

    function showAnswer(answerId) {
        var answer = document.getElementById(answerId);
        answer.style.display = 'block';
    }
</script>
""", unsafe_allow_html=True)
