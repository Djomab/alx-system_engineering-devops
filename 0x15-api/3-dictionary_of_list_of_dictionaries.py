#!/usr/bin/python3
"""Exports data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    """Identifies a user to display completed task info"""
    endpoint = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(endpoint + 'users/').json()
    todos = requests.get(endpoint + 'todos/').json()
    filename = 'todo_all_employees.json'

    dic = {
        str(data.get('id')): [
            {
                'username': data.get('username'),
                'task': item.get('titles'),
                'completed': item.get('completed')
            }
            for item in todos
            if item.get('userId') == data.get('id')
        ]
        for data in users
    }
    with open(filename, 'w') as json_file:
        json.dump(dic, json_file)
