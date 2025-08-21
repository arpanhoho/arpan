from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template_string(open("index.html").read())

@app.route('/calculator')
def calculator():
    return render_template_string(open("calculator.html").read())

@app.route('/tictactoe')
def tictactoe():
    return render_template_string(open("tictactoe.html").read())

@app.route('/style.css')
def css():
    return send_from_directory(".", "style.css")
