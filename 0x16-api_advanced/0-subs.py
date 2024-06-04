#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given,
the function should return 0.
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
    if (reddit_request.status_code != 200
            or 'data' not in reddit_request.json()):
        return 0
    reddit_json = reddit_request.json()
    return reddit_json.get('data').get('subscribers')
