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

def fetch_ids(db):
    query = """
        SELECT DISTINCT
            user_id, twitter_id
        FROM
            resister_user
    """
    res = db.db_manipulate(query=query, fetch=True)
    ret_val = []
    for users in res:
        ret_val.append((users[0],users[1]))
    return ret_val

def detect_new_ac(db, ac_submissions):
    query = """
        SELECT DISTINCT
            problem_id,
            user_id,
            language
        FROM
            ac_submission
    """
    res = set(db.db_manipulate(query=query, fetch=True))
    new_ac = ac_submissions - res
    return new_ac

def insert_new_ac(db, new_ac):
    query = """
        SELECT
            count(*)
        FROM
            ac_submission
    """
    row_id = db.db_manipulate(query=query, fetch=True)[0][0]
    for submisson in new_ac:
        row_id += 1
        query = """
            INSERT INTO
                ac_submission (id, problem_id, user_id, language)
            VALUES(
                %d, '%s', '%s', '%s'
            )
        """ % (row_id, submisson[0], submisson[1], submisson[2])
        db.db_manipulate(query=query, commit=True)

def resister_user(db, user_id, twitter_id, access_token, access_token_secret):
    query = """
        SELECT
            count(*)
        FROM
            resister_user
    """
    row_id = db.db_manipulate(query=query, fetch=True)[0][0] + 1
    query="""
        INSERT INTO
            resister_user (id, user_id, twitter_id, access_token, access_token_secret)
        VALUES(
            %d, '%s', '%s', '%s', '%s'
        )
    """ % (row_id, user_id, twitter_id, access_token, access_token_secret)
    db.db_manipulate(query=query, commit=True)

if __name__ == "__main__":
    db = db_manager.sqlite3manager()
    db.db_create()
    id_pairs = fetch_ids(db)
    res = {}
    for ids in id_pairs:
        user_id = ids[0]
        sub = get_ac_submissions(user_id)
        new_ac = detect_new_ac(db,sub)
        count_new_ac = len(new_ac)
        insert_new_ac(db, new_ac)
        res[user_id] = count_new_ac
    return res
def fetch_ac_count():
    db = db_manager.sqlite3manager()
    db.db_create()
    user_ids = fetch_users(db)
    res = {}
    for user_id in user_ids:
        res[user_id] = len(get_ac_submissions(user_id))
    return res
        
