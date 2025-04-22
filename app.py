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

UPLOAD_FOLDER = '/usr/share'
#UPLOAD_FOLDER = '/Users/hxh/Desktop/test'
UPLOAD_FILE = 'test.txt'
UPLOAD_FILE_PATH = UPLOAD_FOLDER + '/' + UPLOAD_FILE
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FILE'] = UPLOAD_FILE
app.config['UPLOAD_FILE_PATH'] = UPLOAD_FOLDER + '/' + UPLOAD_FILE

@app.route('/submit', methods=['POST'])
def submit():
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = request.form.get('name')
    email = request.form.get('email')
    session['username'] = name
    session['email'] = email
    try:
        with open(UPLOAD_FILE_PATH, 'r', encoding='utf-8') as f:
            all_content = f.read()
    except FileNotFoundError:
        all_content = ''
        with open(UPLOAD_FILE_PATH, 'w', encoding='utf-8') as f:
            pass
    return render_template('index.html', username=session['username'], email=session['email'], all_content=all_content)


@app.route('/upload', methods=['POST'])
def upload_file():
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # file = request.files['file']
    # file.save(f"{UPLOAD_FOLDER}/{session['username']}_{current_time_str}_{file.filename}")
    if request.method == 'POST':
        new_content = f"{session['username']}は[{current_time_str}]に{request.form['content'].strip()}書いた"
        if request.form['content'].strip():
            with open(UPLOAD_FILE_PATH, 'a', encoding='utf-8') as f:
                f.write(new_content + '\n')
    try:
        with open(UPLOAD_FILE_PATH, 'r', encoding='utf-8') as f:
            all_content = f.read()
    except FileNotFoundError:
        all_content = ''
    return render_template('index.html', all_content=all_content)

@app.route('/clear', methods=['POST'])
def clear_file():
    if request.method == 'POST':
        with open(UPLOAD_FILE_PATH, 'w', encoding='utf-8') as f:
           f.write('')
    try:
        with open(UPLOAD_FILE_PATH, 'r', encoding='utf-8') as f:
            all_content = f.read()
    except FileNotFoundError:
        all_content = ''
    return render_template('index.html', all_content=all_content)

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8080)