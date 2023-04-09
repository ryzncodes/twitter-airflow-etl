import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import creds

access_key = creds.API_KEY
access_secret = creds.API_SECRET_KEY
consumer_key = creds.ACCESS_TOKEN
consumer_secret = creds.ACCESS_TOKEN_SECRET

# Twitter authentication
auth = tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_secret)


