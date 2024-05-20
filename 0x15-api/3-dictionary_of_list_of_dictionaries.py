#!/usr/bin/python3
"""returns information about all
    employees and exports data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    # Fetch employee details
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    employees = requests.get(user_url).json()

    all_tasks = {}

    # Iterate over each employee
    for employee in employees:
        employee_id = str(employee.get('id'))
        employee_name = employee.get('username')

        # Fetch employee todo list
        todos_url = (
            f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        )
        employee_tasks = requests.get(todos_url).json()

        # Process tasks
        tasks = [{
            "username": employee_name,
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in employee_tasks]

        # Add to the dictionary with user_id as the key
        all_tasks[employee_id] = tasks

    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
