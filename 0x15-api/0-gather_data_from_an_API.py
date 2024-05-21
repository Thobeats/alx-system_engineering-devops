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
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    user_req = requests.get(user_url)
    user = user_req.json()
    api_req = requests.get(url)
    all_tasks = api_req.json()
    total = len(all_tasks)
    completed_tasks = list(filter(lambda task: task['completed'] is True,
                                all_tasks))
    completed = len(completed_tasks)
    response = "Employee {} is done with tasks({}/{}):\n".format(user['name'],
                                                                completed,
                                                                total)
    for task in completed_tasks:
        response += "   {}\n".format(task['title'])
    print(response)
