#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
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
    filename = "{}.json".format(employee_id)
    with open(filename, 'w', newline='') as file:
        json.dump({employee_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user['username']
        } for task in all_tasks]}, file)
