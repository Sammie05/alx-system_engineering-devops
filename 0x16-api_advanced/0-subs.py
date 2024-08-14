#!/usr/bin/python3

"""This script Queries a redit api and returns the number of suscribers"""

import requests



def number_of_subscribers(subreddit):
    """ Function that returns the number of suscribers from redditapi"""
    url = 'http://www.reddit.com/r/{}/about.json'
    header = {'user-Agent': 'custom'}

    response = requests.get(url.format(subreddit),
                            header, allow_redirects=False)

    if response.status_code == 200:

        subscribers = response.json().get("data").get("subscribers")

        return subscribers

    else:
        print("None")
