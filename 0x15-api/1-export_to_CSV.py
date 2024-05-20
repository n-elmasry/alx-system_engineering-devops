#!/usr/bin/python3
"""returns information about a given employee todo list progress."""
import csv
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

    csv_rows = []

    for task in all_tasks:
        task_title = task.get('title')
        task_completed = task.get('completed')
        csv_rows.append([id, employee_name, task_completed, task_title])

    filename = f'{id}.csv'

    with open(filename, 'w', newline='') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(csv_rows)
