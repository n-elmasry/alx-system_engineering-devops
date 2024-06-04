#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
import json
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about/.json'.format(
        subreddit)
    info = requests.get(url,
                        headers={"user-agent": "user"},
                        allow_redirects=False).json()
    if "data" not in info:
        return 0
    subscribers = info.get('data').get('subscribers')
    return subscribers
