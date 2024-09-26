#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def number_of_subscribers(subreddit):
    '''Retrieves the number of subscribers in a given subreddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': 'MyRedditApp/0.1 by Sammie05'
    }
    res = requests.get(
        '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        try:
            return res.json()['data']['subscribers']
        except KeyError:
            return 0
    return 0

