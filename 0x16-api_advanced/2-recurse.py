#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles for a given subreddit
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ returns a list containing the titles of all hot articles"""
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    info = requests.get(url,
                        headers={"user-agent": "user"},
                        allow_redirects=False).json()
    if "data" not in info and hot_list == []:
        return None
    posts = info.get("data").get("children")
    for post in posts:
        hot_list.append(post.get("data").get("title"))
        count += 1
    after = info.get("data").get("after")
    if after is None:
        return hot_list
    return (recurse(subreddit, hot_list, after, count))
