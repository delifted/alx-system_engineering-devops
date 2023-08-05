#!/usr/bin/python3

"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""

import csv
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API, id)).json()
            todos_res = requests.get('{}/todos'.format(API)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))

            csv_file_name = '{}.csv'.format(id)

            with open(csv_file_name, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

                for todo in todos:
                    csv_writer.writerow(
                            [id, user_name, todo['completed'], todo['title']])
