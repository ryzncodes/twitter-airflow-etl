import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import creds

def run_twitter_etl():

    access_key = creds.API_KEY
    access_secret = creds.API_SECRET_KEY
    consumer_key = creds.ACCESS_TOKEN
    consumer_secret = creds.ACCESS_TOKEN_SECRET

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key,access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    # API Object
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name = '@AzriWalter',
                            count = 200,
                            include_rts = False,
                            tweet_mode = 'extended' #Extended to keep the full tweet text.
                            )

    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {'user': tweet.user.screen_name,
                        'text' : text,
                        'favorite_count': tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("azriwalter_twitter_data.csv")