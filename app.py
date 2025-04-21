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

#UPLOAD_FOLDER = '/usr/share/text.txt'
UPLOAD_FOLDER = '/Users/hxh/Desktop/test/test.txt'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/submit', methods=['POST'])
def submit():
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = request.form.get('name')
    email = request.form.get('email')
    session['username'] = name
    session['email'] = email
    try:
        with open(UPLOAD_FOLDER, 'r', encoding='utf-8') as f:
            all_content = f.read()
    except FileNotFoundError:
        all_content = ''
    return render_template('index.html', username=session['username'], email=session['email'], all_content=all_content)


@app.route('/upload', methods=['POST'])
def upload_file():
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # file = request.files['file']
    # file.save(f"{UPLOAD_FOLDER}/{session['username']}_{current_time_str}_{file.filename}")
    if request.method == 'POST':
        new_content = request.form['content'].strip()
        if new_content:
            with open(UPLOAD_FOLDER, 'a', encoding='utf-8') as f:
                f.write(new_content + '\n')
    # 读取全部内容显示
    try:
        with open(UPLOAD_FOLDER, 'r', encoding='utf-8') as f:
            all_content = f.read()
    except FileNotFoundError:
        all_content = ''
    return render_template('index.html', all_content=all_content)

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8080)