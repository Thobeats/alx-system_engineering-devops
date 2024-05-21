#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
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
    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, user['username'], task['completed'], task['title']]
        ) for task in all_tasks]
