#!/usr/bin/python3
'''
using REST API, for a given employee ID,
returns information about his/her TODO list progress
'''
from sys import argv
import requests
from sqlalchemy import true

if __name__ == "__main__":
    user_id = argv[1]
    users_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    todos_url = 'https://jsonplaceholder.typicode.com/todos/'
    users_data = requests.get(users_url)
    name = users_data.json().get('name')

    todos_data = requests.get(todos_url)
    todos_id = todos_data.get('userId')
    done_tasks = todos_data.get('completed')
    tasks = len(todos_data)
    done_count = 0
    title = todos_data.get('title')

    task_title = []

    for i in todos_data:
        if todos_id == user_id:
            if done_tasks == true:
                task_title.append(i[title])
            done_count += 1

    print('Employee {} is done with tasks(NUMBER_OF_DONE_TASKS/{}})'.format(name, done_tasks,tasks))
    for x in task_title:
          print("\t {}".format(x))
