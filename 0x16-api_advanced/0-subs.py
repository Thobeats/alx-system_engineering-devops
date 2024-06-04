#!/usr/bin/python3
"""
Write a function that queries the
Reddit API and prints the titles
of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Number of Subreddit Subscribers
    Keyword arguments:
    subreddit -- the subreddit to check e.g programming.
    Return: the number of subscribers or 0 if the subreddit doesn't exist
    """
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {"user-agent": "user"}
    reddit_request = requests.get(url,
                                  headers=headers,
                                  allow_redirects=False)
    if reddit_request.status_code != 200:
        return 0
    reddit_json = reddit_request.json()
    return reddit_json.get('data').get('subscribers')
