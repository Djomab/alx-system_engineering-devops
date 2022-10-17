#!/usr/bin/python3
"""Exports user in the JSON format."""
import json
import requests

if __name__ == "__main__":
    """Identifies a user to display completed task info"""
    endpoint = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(endpoint + 'users/').json()
    todos = requests.get(endpoint + 'todos/').json()
    filename = 'todo_all_employees.json'

    dic = {
        str(user.get('id')): [
            {
                'username': user.get('username'),
                'task': item.get('title'),
                'completed': item.get('completed')
            }
            for item in todos
            if item.get('userId') == user.get('id')
        ]
        for user in users
    }
    with open(filename, 'w') as json_file:
        json.dump(dic, json_file)
