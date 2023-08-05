#!/usr/bin/python3

import requests
import sys
import re

"""
def get_employee_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        response = requests.get(f"{base_url}/users/employee_id")
        response.raise_for_status()
        user_data = response.json()
        employee_name = user_data['name']

        response = requests.get(f"{base_url}/todos?userId={employee.id}")
        response.raise_for_status()
        todo_list = response.json()

        total_tasks = len(todo_list)
        completed_tasks = [task for task in todo_list if task['completed']]
        num_completed_tasks = len(completed_tasks)

        print(f"Employee {employee_name} is done with tasks(
                {num_completed_tasks}/{total_tasks}:")

        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except Exception as ex:
        print("An error occured:", ex)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)


        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
"""
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""

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
            todos_done = list(filter(lambda x: x.get('completed'), todos))

            print(
                    'Employee {} is done with tasks({}/{}):'.format(
                        user_name,
                        len(todos_done),
                        len(todos)
                        )
                    )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
