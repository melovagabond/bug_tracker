from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def track():
    name = 'Joe'
    return render_template('staticfiles/html/index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')