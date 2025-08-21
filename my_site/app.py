from flask import Flask
import webbrowser
import threading

app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return open("index.html").read()

# About page route 
@app.route("/about") 
def about(): 
    return "<h1>About Page</h1><p>Python just for fun haha.</p>"

# Calculator page route
@app.route("/calculator")
def calculator():
    return open("calculator.html").read()

# Tictactoe page route
@app.route("/tictactoe")
def tictactoe():
    return open("tictactoe.html").read()

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True, host="127.0.0.1", port=5000)

