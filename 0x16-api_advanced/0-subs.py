#!/usr/bin/python3

"""
Python Script Fetch API
"""

import requests


def number_of_subscribers(subreddit):
    '''Construct the URL to query the subreddit's information'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to prevent Too Many Requests error
    headers = {"User-Agent": "Custom Reddit Subscribers Checker"}

    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        response_json = response.json()

        # Check if the response contains subscriber count
        if "data" in response_json and "subscribers" in response_json["data"]:
            return response_json["data"]["subscribers"]
        else:
            return 0  # Invalid subreddit or missing subscriber count
    except requests.exceptions.RequestException:
        return 0  # Error occurred, return 0


'''# Example usage
if __name__ == "__main__":
    subreddit_name = "programming"  # Replace with the desired subreddit
    print(number_of_subscribers(subreddit_name))
'''
