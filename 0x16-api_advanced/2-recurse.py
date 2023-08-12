#!/usr/bin/python3
'''Recursive Function for API'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    # Base URL for querying hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to prevent Too Many Requests error
    headers = {"User-Agent": "Custom Reddit Recursive Posts Collector"}

    # Parameters for the API request, including the "after"
    # parameter for pagination
    params = {"limit": 100, "after": after}

    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=params)
        response_json = response.json()

        # Check if the response contains posts
        if "data" in response_json and "children" in response_json["data"]:
            posts = response_json["data"]["children"]

            # Append the titles of the current page's hot posts to the list
            for post in posts:
                hot_list.append(post["data"]["title"])

            # Check if there's another page of hot posts
            if "data" in response_json and "after" in response_json["data"]\
                    and response_json["data"]["after"] is not None:
                # Recursively call the function with the "after"
                # parameter to retrieve the next page
                return recurse(subreddit, hot_list,
                               response_json["data"]["after"])
            else:
                # No more pages, return the complete hot_list
                return hot_list
        else:
            return None  # Invalid subreddit or no posts
    except requests.exceptions.RequestException:
        return None  # Error occurred, return None
