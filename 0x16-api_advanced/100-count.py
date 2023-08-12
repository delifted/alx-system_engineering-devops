#!/usr/bin/python3
'''
Recursive Function to count words from API fetch
'''

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    # Base URL for querying hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to prevent Too Many Requests error
    headers = {"User-Agent": "Custom Reddit Word Counter"}

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

            # Count words in the current page's hot posts
            for post in posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    if title.count(word.lower()) > 0:
                        # Increment word count
                        if word in word_count:
                            word_count[word] += title.count(word.lower())
                        else:
                            word_count[word] = title.count(word.lower())

            # Check if there's another page of hot posts
            if "data" in response_json and "after" in\
            response_json["data"] and response_json["data"]["after"]\
            is not None:
                # Recursively call the function with the "after"
                # parameter to retrieve the next page
                return count_words(subreddit, word_list,
                                   response_json["data"]["after"], word_count)
            else:
                # No more pages, print the sorted word count
                sorted_word_count = sorted(word_count.items(),
                                           key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
        else:
            print("None")  # Invalid subreddit or no posts
    except requests.exceptions.RequestException:
        print("None")  # Error occurred, print None
