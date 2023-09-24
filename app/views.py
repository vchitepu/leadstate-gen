from app import app
from flask import render_template

@app.route('/')
def main():
    return "Hello!"

@app.route('/home')
def home():
    return render_template('home.html')

