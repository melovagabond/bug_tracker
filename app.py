from flask import Flask, render_template, url_for, json
import requests

app = Flask(__name__)

@app.route('/')
def track():
    return "Track Some bugs!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')