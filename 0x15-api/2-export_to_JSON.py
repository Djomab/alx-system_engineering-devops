#!/usr/bin/python3
"""Exports data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    """Identifies a user to display completed task info"""
    endpoint = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user = requests.get(endpoint + 'users/{}'.format(userId)).json()
    userTodos = requests.get(endpoint + 'users/{}/todos'.format(userId)).json()
    filename = userId + '.json'

    with open(filename, 'w', newline='', encoding='UTF8') as f:
        json.dump({
            userId:
                [{
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username")}
                 for task in userTodos]},
            f)
