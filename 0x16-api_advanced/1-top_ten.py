#!/usr/bin/python3
"""
API Request to get Top Ten
"""

import requests


def top_ten(subreddit):
    '''Construct the URL to query the subreddit's hot posts'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to prevent Too Many Requests error
    headers = {"User-Agent": "Custom Reddit Top Ten Posts Viewer"}

    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        response_json = response.json()

        # Check if the response contains posts
        if "data" in response_json and "children" in response_json["data"]:
            posts = response_json["data"]["children"]

            # Print the titles of the first 10 hot posts
            for index, post in enumerate(posts[:10], start=1):
                print(f"{post['data']['title']}")
        else:
            print("None")  # Invalid subreddit or no posts
    except requests.exceptions.RequestException:
        print("None")  # Error occurred, print None


'''
# Example usage
if __name__ == "__main__":
    subreddit_name = "programming"  # Replace with the desired subreddit
    top_ten(subreddit_name)
'''
