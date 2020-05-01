import os
import requests
import pprint
import psycopg2

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

def detect_new_ac(rows, ac_submissions):
    new_ac = ac_submissions
    return new_ac

sub = get_ac_submissions(user_id='yoshizou')
print(sub)