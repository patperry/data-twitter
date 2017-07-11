#!/usr/bin/env python3

# need consumer and access tokens first, set up in access.sh;

# adapted from https://github.com/bear/python-twitter/blob/master/examples/streaming/track_users.py

import os
import json
import time

from twitter import Api

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY", None)
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET", None)
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", None)
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", None)

HASHTAGS = ['#rstats']

api = Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def main():
    print('Started on ' + time.strftime('%c'))
    try:
        with open('rstats-tweets.json', 'a') as f:
            for line in api.GetStreamFilter(track=HASHTAGS):
                f.write(json.dumps(line))
                f.write('\n')
                print(line['user']['screen_name'] + ': ' + line['text'])

    except KeyboardInterrupt:
        print('Stopped on ' + time.strftime('%c'))

if __name__ == '__main__':
    main()
