from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']
    response = requests.post('http://localhost:5001/login', json={'email': email, 'senha': senha})
    if response.status_code == 200:
        return redirect('/dashboard')
    return 'Login falhou', 401
