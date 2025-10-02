# Import the Flask class from the flask module
from flask import Flask

# Create a new Flask web application instance
# __name__ ensures the app knows where it is located
app = Flask(__name__)

# Define a route for the root URL ("/")
# When a user visits the root URL, this function is called
@app.route("/")
def home():
    # Return a simple message to display on the web page
    return "Hello! 🎉 This is my Python website running on EC2."

# Define a dynamic route to add two numbers
# <int:a> and <int:b> capture integer values from the URL
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    # Return the sum of the two numbers as a string
    return f"The sum of {a} and {b} is {a+b}"

# This ensures the code runs only if this script is executed directly,
# and not if it is imported as a module in another script
if __name__ == "__main__":
    # Run the Flask development server
    # host="0.0.0.0" allows the server to be accessible externally (important for EC2)
    # port=5000 specifies the port to listen on
    app.run(host="0.0.0.0", port=5000)
