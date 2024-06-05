#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Number of Subreddit Subscribers
    Keyword arguments:
    subreddit -- the subreddit to check e.g programming.
    Return: the number of subscribers or 0 if the subreddit doesn't exist
    """
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {"user-agent": "user"}
    reddit_request = requests.get(url,
                                  headers=headers,
                                  allow_redirects=False)
    if (reddit_request.status_code != 200):
        return 0
    reddit_json = reddit_request.json()
    if 'data' not in reddit_json:
        return 0
    return reddit_json.get('data').get('subscribers')
