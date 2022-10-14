import pandas as pd
import numpy as np

import os
import time
import requests
import json
import csv
from tqdm import tqdm

import tweepy

import requests
import pandas as pd
import os

from collections import Counter
import matplotlib.pyplot as plt

consumer_key        = 'vkbw3D6WAihxpRS4vr9EErE3X'
consumer_secret     = 'QIJk5ofe72ojQ2QTeCBeIF8su69boVaC4hHzblCaXwqLy9hsVg'
access_token        = '1568081688521064450-CRb8ArAF46VJ0n3JoImfKLPFIwy6Fi'
access_token_secret = 'gHKwHP7GLMcLIao0B1xj7qZKbfgoAJc6e5qvmmbCuHN3l'
bearer_token        = 'AAAAAAAAAAAAAAAAAAAAAFCFgwEAAAAAoKDpL0OY%2BaVesVnzOqfMPIpQaVI%3DuYiaktsSQXU9W2mwT0sU1PW0B50mZj8PeudBxc23fx6vJ4z3UB'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
headers = {"Authorization": "Bearer {}".format(bearer_token)}

# Add the search_twitter function here.
def search_twitter(query, max_results, bearer_token, start_time, end_time, tweet_fields):
    client = tweepy.Client(bearer_token=bearer_token)
    tweets = tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=tweet_fields, start_time=start_time, end_time=end_time).flatten(limit = max_results)
    tweet_search = []
    for tweet in tweets:
        tweet_search.append((tweet.text, tweet.author_id, tweet.created_at, tweet.lang))

    return tweet_search

query = '#savetheplanet'
max_results=500
start_time = '2022-10-05T00:00:00Z'
end_time = '2022-10-10T00:00:00Z'
tweet_fields = 'text,author_id,created_at,lang'
climate_search = search_twitter(query, max_results, bearer_token, start_time, end_time, tweet_fields)
#convert to dataframe
climate_df = pd.DataFrame(climate_search, columns=['text', 'author_id', 'created_at', 'lang'])
climate_df.head()
#save to csv
climate_df.to_csv('data/saveplanet_data.csv', index=False)