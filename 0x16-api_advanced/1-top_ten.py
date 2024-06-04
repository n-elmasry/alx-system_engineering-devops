#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests
import json


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit)
    info = requests.get(url,
                        headers={"user-agent": "user"},
                        allow_redirects=False).json()
    if 'data' not in info:
        print('None')
        return
    posts = info.get('data').get('children')
    for post in posts:
        print(post.get('data').get('title'))
