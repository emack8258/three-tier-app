from flask import Flask
# Create an instance of the Flask class
app = Flask(__name__)
API_URL = 'http://localhost:3000/'

@app.route('/') # Maps URL path to Python function
def hello():
    return "<p>Hello World!</>"

