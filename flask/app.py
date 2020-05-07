from flask import Flask, render_template, request
import sys
sys.path.append('../src')
from db_manager import sqlite3manager
from fetch_submission import fetch_users, resister_user

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return render_template('index.html',
        message = '登録するユーザIDを入力してください。')

@app.route('/', methods=['POST'])
def post():
    db = sqlite3manager(db_path='../database.sqlite3')
    user_id = request.form['name']
    users = fetch_users(db)
    if user_id in users:
        message = '{}さんはすでに登録されています。'.format(user_id)
    else:
        resister_user(db, user_id)
        message = '{}さんの登録が完了しました！'.format(user_id)
    return render_template('index.html', message = message)


if __name__ == "__main__":
    app.run(host='0.0.0.0')