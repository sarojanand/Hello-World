from flask import Flask
import webbrowser
from threading import Timer

app = Flask(__name__)

# Function to open the default web browser automatically
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

# Define the home route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Main function to run the Flask app and open the browser
if __name__ == "__main__":
    # Set a timer to open the browser shortly after the Flask app starts
    Timer(1, open_browser).start()
    # Run the Flask app
    app.run(debug=True)
