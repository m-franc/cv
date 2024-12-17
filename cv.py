from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Site de maxime Franc!</p>"

@app.route("/cv")
def cv():
    return render_template('cv.html')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('cv'))
