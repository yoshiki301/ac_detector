import tweepy
import time

CONSUMER_KEY=""
CONSUMER_SECRET=""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

ut = time.time() #時刻の取得
strin = "tweepyからツイート"
api.update_status(strin)
print(strin)

