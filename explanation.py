<div class="hero-section">
    <h1 class="glowing-title">📚 Chemistry Concepts & Explanation</h1>
</div>

<div class="topic-selection">
    <h2>Select a topic to learn about:</h2>
    <div class="topic-cards">
        <div class="topic-card" onclick="toggleDetails('ph-details')">pH</div>
        <div class="topic-card" onclick="toggleDetails('poh-details')">pOH</div>
        <div class="topic-card" onclick="toggleDetails('molarity-details')">Molarity</div>
    </div>
</div>

<!-- Details Section -->
<div id="ph-details" class="details hidden">
    <h3>Understanding pH</h3>
    <p>What is pH? pH is a measure of the hydrogen ion concentration in a solution...</p>
    <h4>Test Your Knowledge! 📝</h4>
    <form>
        <label>What pH value represents a neutral solution?</label><br>
        <input type="radio" name="ph" value="0"> 0<br>
        <input type="radio" name="ph" value="7"> 7<br>
        <input type="radio" name="ph" value="14"> 14<br>
        <input type="radio" name="ph" value="3.5"> 3.5<br>
        <button type="button" onclick="showCorrectAnswer('ph', 7)">Submit</button>
    </form>
    <div id="ph-correct" class="correct-answer hidden">The correct one is 7</div>
</div>

<div id="poh-details" class="details hidden">
    <h3>Understanding pOH</h3>
    <p>What is pOH? pOH is a measure of the hydroxide ion concentration in a solution...</p>
    <h4>Test Your Knowledge! 📝</h4>
    <form>
        <label>What pOH value represents a neutral solution?</label><br>
        <input type="radio" name="poh" value="0"> 0<br>
        <input type="radio" name="poh" value="7"> 7<br>
        <input type="radio" name="poh" value="14"> 14<br>
        <input type="radio" name="poh" value="3.5"> 3.5<br>
        <button type="button" onclick="showCorrectAnswer('poh', 7)">Submit</button>
    </form>
    <div id="poh-correct" class="correct-answer hidden">The correct one is 7</div>
</div>

<div id="molarity-details" class="details hidden">
    <h3>Understanding Molarity</h3>
    <p>What is Molarity? Molarity (M) is a measure of the concentration of a solution...</p>
    <h4>Test Your Knowledge! 📝</h4>
    <form>
        <label>If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?</label><br>
        <input type="radio" name="molarity" value="0.5"> 0.5 M<br>
        <input type="radio" name="molarity" value="1.0"> 1.0 M<br>
        <input type="radio" name="molarity" value="2.0"> 2.0 M<br>
        <input type="radio" name="molarity" value="4.0"> 4.0 M<br>
        <button type="button" onclick="showCorrectAnswer('molarity', 4)">Submit</button>
    </form>
    <div id="molarity-correct" class="correct-answer hidden">The correct one is 4</div>
</div>
