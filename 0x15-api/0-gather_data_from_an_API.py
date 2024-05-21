#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(url, employee_id)
    todo = "{}/users/{}/todos".format(url, employee_id)
    user_req = requests.get(user_url)
    user = user_req.json()
    api_req = requests.get(todo)
    all_tasks = api_req.json()
    total = len(all_tasks)
    completed_tasks = list(filter(lambda task: task['completed'] is True,
                                  all_tasks))
    completed = len(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(user['name'],
                                                          completed,
                                                          total))
    for task in completed_tasks:
        print("\t {}".format(task['title']))
