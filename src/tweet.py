import tweepy
import time
import fetch_submission

if __name__ == '__main__':
    CONSUMER_KEY=""
    CONSUMER_SECRET=""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    memo = fetch_submission.fetch_new_ac_count()
    strin = "昨日のAC数を自動ツイート\n"
    for user in memo:
        strin += user+":" + str(memo[user]) + "\n"
    api.update_status(strin)
    print(strin)
    print("を出力")

