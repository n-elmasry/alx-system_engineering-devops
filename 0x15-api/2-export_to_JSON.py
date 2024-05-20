#!/usr/bin/python3
"""returns information about a given employee and
    export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":

    id = argv[1]

    # Fetch employee details
    user_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    employee = requests.get(user_url).json()
    employee_name = employee.get('username')

    # Fetch employee todo list
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
    all_tasks = requests.get(todos_url).json()

    # Process tasks
    done_tasks = [task.get('title')
                  for task in all_tasks if task.get('completed')]

    tasks = [{
        "task": task.get('title'),
        "completed": task.get('completed'),
        "username": employee_name
    } for task in all_tasks]

    data = {id: tasks}

    with open(f'{id}.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
