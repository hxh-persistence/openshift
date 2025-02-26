from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'hxhtest'
# @app.route("/")
# def home():
#     items = [
#         {"title":"test_title1", "description":"test_description1"},
#         {"title":"test_title2", "description":"test_description2"} 
#     ]
#     return render_template('index.html', title='Welcome Page', name='john doe', items = items)

@app.route('/')
def login():
    return render_template('login.html', title='Login Page')

@app.route('/submit', methods=['POST'])
def submit():
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = request.form.get('name')
    email = request.form.get('email')
    session['username'] = name
    session['email'] = email
    return render_template('index.html', username=session["username"], email=session["email"])

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8080)