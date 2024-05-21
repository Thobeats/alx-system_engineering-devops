#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    todos = requests.get("{}/todos".format(url)).json()
    filename = "todo_all_employees.json"
    with open(filename, 'w', newline='') as file:
        json.dump({user["id"]: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user['username']
        } for task in todos if task['userId'] == user['id']]
            for user in users}, file)
