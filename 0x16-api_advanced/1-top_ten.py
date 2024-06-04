#!/usr/bin/python3
"""
Write a function that queries the
Reddit API and prints the titles
of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API
    prints the titles of the first 10 hot posts for subreddit
    Keyword arguments:
    subreddit -- the subreddit to check e.g programming.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"user-agent": "user"}
    reddit_request = requests.get(url,
                                  headers=headers,
                                  allow_redirects=False)
    if (reddit_request.status_code != 200):
        print('None')
        return
    reddit_json = reddit_request.json()
    for reddit in reddit_json['data']['children']:
        print(reddit.get('data').get('title'))
