# ============================================
# Flask Button-Based Calculator
# ============================================

from flask import Flask, render_template_string

app = Flask(__name__)

# HTML + CSS + JavaScript in one template (for simplicity)
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Button Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        .calculator { display: inline-block; margin-top: 50px; }
        input { width: 220px; height: 50px; text-align: right; font-size: 20px; margin-bottom: 10px; }
        button { width: 50px; height: 50px; font-size: 18px; margin: 3px; }
    </style>
</head>
<body>
    <h1>🧮 Flask Online Calculator</h1>
    <div class="calculator">
        <input type="text" id="display" disabled>
        <br>
        <!-- Row 1 -->
        <button onclick="press('7')">7</button>
        <button onclick="press('8')">8</button>
        <button onclick="press('9')">9</button>
        <button onclick="press('/')">÷</button>
        <br>
        <!-- Row 2 -->
        <button onclick="press('4')">4</button>
        <button onclick="press('5')">5</button>
        <button onclick="press('6')">6</button>
        <button onclick="press('*')">×</button>
        <br>
        <!-- Row 3 -->
        <button onclick="press('1')">1</button>
        <button onclick="press('2')">2</button>
        <button onclick="press('3')">3</button>
        <button onclick="press('-')">−</button>
        <br>
        <!-- Row 4 -->
        <button onclick="press('0')">0</button>
        <button onclick="press('.')">.</button>
        <button onclick="calculate()">=</button>
        <button onclick="press('+')">+</button>
        <br>
        <!-- Row 5 -->
        <button onclick="clearDisplay()" style="width: 220px;">C</button>
    </div>

    <script>
        function press(value) {
            document.getElementById('display').value += value;
        }

        function calculate() {
            try {
                let result = eval(document.getElementById('display').value);
                document.getElementById('display').value = result;
            } catch (e) {
                document.getElementById('display').value = "Error";
            }
        }

        function clearDisplay() {
            document.getElementById('display').value = "";
        }
    </script>
</body>
</html>
"""

@app.route("/")
def calculator():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    # host=0.0.0.0 makes it accessible on Elastic IP
    app.run(debug=True, host="0.0.0.0", port=5000)
