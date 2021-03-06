import os
import requests
import pprint
import db_manager

def get_ac_submissions(user_id):
    url = 'https://kenkoooo.com/atcoder/atcoder-api/results?user=%s' % user_id
    r_get = requests.get(url)
    ac_submissions = set()
    for submission in r_get.json():
        if submission['result'] == 'AC':
            ac_submission = (
                submission['problem_id'],
                submission['user_id'],
                submission['language']
            )
            ac_submissions.add(ac_submission)
    return ac_submissions

def fetch_users(db):
    query = """
        SELECT DISTINCT
            user_id
        FROM
            resister_user
    """
    res = db.db_manipulate(query=query, fetch=True)
    user_ids = []
    for users in res:
        user_ids.append(users[0])
    return user_ids

def detect_new_ac(db, ac_submissions):
    query = """
        SELECT DISTINCT
            problem_id,
            user_id,
            language
        FROM
            ac_submisson
    """
    res = set(db.db_manipulate(query=query, fetch=True))
    new_ac = ac_submissions - res
    return new_ac

def insert_new_ac(db, new_ac):
    query = """
        SELECT
            count(*)
        FROM
            ac_submisson
    """
    row_id = db.db_manipulate(query=query, fetch=True)[0][0]
    for submisson in new_ac:
        row_id += 1
        query = """
            INSERT INTO
                ac_submisson (id, problem_id, user_id, language)
            VALUES(
                %d, '%s', '%s', '%s'
            )
        """ % (row_id, submisson[0], submisson[1], submisson[2])
        db.db_manipulate(query=query, commit=True)

if __name__ == "__main__":
    db = db_manager.sqlite3manager()
    db.db_create()
    user_ids = fetch_users(db)
    res = {}
    for user_id in user_ids:
        sub = get_ac_submissions(user_id)
        new_ac = detect_new_ac(db,sub)
        count_new_ac = len(new_ac)
        insert_new_ac(db, new_ac)
        res[user_id] = count_new_ac
    print(res)