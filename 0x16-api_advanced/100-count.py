#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted
count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, hot_list={}, after="", dist=""):
    """
    queries the Reddit API,
    parses the title of all hot articles, and prints a sorted
    count of given keywords
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
        print()
        return
    reddit_json = reddit_request.json()
    after = reddit_json['data']['after']
    dist = reddit_json['data']['dist']
    for reddit in reddit_json['data']['children']:
        title = reddit.get('data').get('title')
        for word in word_list:
            if word not in hot_list.keys():
                hot_list[word] = 0
            hot_list[word] += title.lower().count(word.lower())
    if after is not None:
        return count_words(subreddit, word_list, hot_list, after, dist)
    sorted_keys = list(hot_list.keys())
    sorted_keys.sort()
    for kys in sorted_keys:
        if hot_list[kys] != 0:
            print("{}: {}".format(kys, hot_list[kys]))
