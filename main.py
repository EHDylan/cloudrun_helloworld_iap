# main.py
from flask import Flask
import os

# The buildpack will look for a variable named 'app'
app = Flask(__name__)

@app.route('/')
def hello_world():
    port = os.environ.get('PORT', '8080')
    return f'Hello World! I am running on port {port}.'
