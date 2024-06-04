#!/usr/bin/python3
"""
defines function to query the Reddit API for
prints titles of the first 10 hot posts
"""
import json
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts for subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit)
    info = requests.get(url,
                        headers={"user-agent": "user"},
                        allow_redirects=False).json()
    if "data" not in info:
        print("None")
        return
    posts = info.get("data").get("children")
    for post in posts:
        print(child.get("data").get("title"))
