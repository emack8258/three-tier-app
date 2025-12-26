from flask import Flask, render_template, request, redirect, url_for
import requests
import os

# Create an instance of the Flask class
app = Flask(__name__)
API_URL = os.getenv('API_URL', 'http://backend:7000/api/text-docs/')

@app.route('/') # Maps URL path to Python function
def index():
    # Fetch data from Django Backend
    response = requests.get(API_URL)

    data = response.json()
    
    # Flask will look for templates in the templates folder
    return render_template('index.html', documents=data)

@app.route('/add', methods=['POST'])
def add_text():
    text_content = request.form.get('content')
    # Send data to Django Backend
    requests.post(API_URL, json={"content": text_content})

    # Redirect the endpoint
    return redirect(url_for('index'))

# Error page handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404