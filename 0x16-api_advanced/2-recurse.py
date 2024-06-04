#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if type(subreddit) is not str:
        return None
    sub = subreddit
    url = "https://api.reddit.com/r/{}/hot?after={}".format(sub, after)
    headers = {"user-agent": "user"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        after = response.json()["data"]["after"]
        if after is None:
            hot_list = titles(posts, len(posts))
            return hot_list
        hot_list.append(recurse(subreddit, hot_list, after=after))
        hot_list = titles(posts, len(posts))
    else:
        return None
    return hot_list


def titles(hot_list, length, titles_list=[]):
    """
    Gets titles of posts from the data
    """
    if length == 0:
        return titles_list
    titles_list.append(hot_list[length - 1]["data"]["title"])
    return titles(hot_list, length - 1, titles_list)
