from flask import Flask, render_template, request
import sys
sys.path.append('../src')
from db_manager import sqlite3manager
from fetch_submission import fetch_ids, resister_user

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return render_template('index.html',
        message = '登録するユーザIDとTwitterIDを入力してください。')

@app.route('/', methods=['POST'])
def post():
    db = sqlite3manager(db_path='../database.sqlite3')
    user_id = request.form['atcoder']
    twitter_id = request.form['twitter']
    id_pairs = fetch_ids(db)
    resistered_user_ids = []
    resisteres_twitter_ids = []
    for ids in id_pairs:
        resistered_user_ids.append(ids[0])
        resisteres_twitter_ids.append(ids[1])

    if user_id in resistered_user_ids or twitter_id in resisteres_twitter_ids:
        message = 'ユーザIDかTwitterIDが登録済みです。'
    else:
        #ここでaccess_tokenを発行
        #resister_user(db, user_id)
        message = '{}さんの登録が完了しました！'.format(user_id)
    return render_template('index.html', message = message)


if __name__ == "__main__":
    app.run(host='0.0.0.0')