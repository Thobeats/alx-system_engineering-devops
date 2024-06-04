#!/usr/bin/python3
"""
Write a recursive function that queries
the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after="", dist=""):
    """
    queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    Keyword arguments:
    subreddit -- the subreddit to check e.g programming.
    Return: a list of titles, None if no results are found
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "user"}
    params = {
        "limit": 100,
        "after": after,
        "count": dist
    }
    reddit_request = requests.get(url,
                                  headers=headers,
                                  params=params,
                                  allow_redirects=False)
    if (reddit_request.status_code != 200):
        return None
    reddit_json = reddit_request.json()
    after = reddit_json['data']['after']
    dist = reddit_json['data']['dist']
    for reddit in reddit_json['data']['children']:
        hot_list.append(reddit.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after, dist)
    return hot_list
