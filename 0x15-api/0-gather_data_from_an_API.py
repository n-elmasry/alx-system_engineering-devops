#!/usr/bin/python3
"""returns information about a given employee TODO list progress."""
import requests
from sys import argv

id = argv[1]

# Fetch employee details
user_url = f'https://jsonplaceholder.typicode.com/users/{id}'
employee = requests.get(user_url).json()
employee_name = employee.get('name')

# Fetch employee TODO list
todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
all_tasks = requests.get(todos_url).json()

# Process tasks
done_tasks = [task.get('title') for task in all_tasks if task.get('completed')]


print(
    f'Employee {employee_name} is done with tasks({len(done_tasks)}/'
    f'{len(all_tasks)}):'
)

# Print each completed task
for task in done_tasks:
    print(f'\t {task}')
