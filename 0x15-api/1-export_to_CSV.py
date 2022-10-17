#!/usr/bin/python3
"""returns information about TODO list progress of a given employee"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    """Identifies a user to display completed task info"""
    endpoint = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user = requests.get(endpoint + 'users/{}'.format(userId)).json()
    userTodos = requests.get(endpoint + 'users/{}/todos'.format(userId)).json()
    filename = userId + '.csv'

    with open(filename, 'w', newline='', encoding='UTF8') as f:
        for task in userTodos:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow([int(userId),
                            user.get('username'),
                            task.get('completed'),
                            task.get('title')])
