from datetime import datetime
import json


# read data from the json file
def read_data():
    try:
        with open('tasks.json', 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("JSON file is not an array!")
            else:
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# add data to the json file
def write_data(data):
    with open("tasks.json", 'w') as f:
        json.dump(data, f, indent=4)


# task manager functionality
class TaskManager:
    # list tasks
    @staticmethod
    def list_all():
        tasks = read_data()
        for task in tasks:
            print(task)

    # add new task
    @staticmethod
    def add_task(task_name, descript):
        tasks = read_data()
        if tasks:
            next_id = max(task['_id'] for task in tasks) + 1
        else:
            next_id = 1
        task_doc = {
            '_id': next_id,
            "task": task_name,
            "description": descript,
            "status": 'todo',
            "created_at": datetime.now().isoformat(),
            "updated_at": None
        }

        tasks = read_data()

        tasks.append(task_doc)

        write_data(tasks)
        print(f"task with id: {next_id} has been added!")

    # update task base on id
    @staticmethod
    def update_task(tsk_id, new_task_name):
        tsk_id = int(tsk_id)
        tasks = read_data()
        for task in tasks:
            if task['_id'] == tsk_id:
                task['task'] = new_task_name
                task['updated_at'] = datetime.now().isoformat()

        write_data(tasks)
        print(f"task with id {tsk_id} has been updated!")

    #  delete task based on id
    @staticmethod
    def delete_task(_id):
        _id = int(_id)
        tasks = read_data()
        tasks = list(filter(lambda x: x['_id'] != _id, tasks))
        write_data(tasks)
        print(f"task with id: {_id} has been deleted!")

    # mark task as done or in-progress
    @staticmethod
    def mark_task(_id, _type):
        _id = int(_id)
        tasks = read_data()
        for task in tasks:
            if task['_id'] == _id:
                task['status'] = _type

        write_data(tasks)

        print(f'task with id: {_id} has been marked as {_type}')

    @staticmethod
    def list_task(_type):
        tasks = read_data()
        for task in tasks:
            if task['status'] == _type:
                print(task)


list_commands = [
    'task-cli list',
    'task-cli add',
    'task-cli update',
    'task-cli delete',
    'task-cli mark',
    "task-cli quit"
]


def running():
    print("Welcome to Task Manager! \n")
    while True:
        print("List of available commands")
        for command in list_commands:
            print(command)
        print('\n')
        choice = input("Enter command: ")

        if choice.startswith("task-cli"):
            command = choice[9:]
            if command.startswith('add'):
                task_name = command[4:]
                description = input("Enter task description: ")

                TaskManager.add_task(task_name, description)
            elif command.startswith("list"):
                if command == 'list':
                    TaskManager.list_all()
                else:
                    _type = command[5:]
                    TaskManager.list_task(_type)

            elif command.startswith('update'):
                _id = command[7:9]
                new_task_name = command[9:]
                TaskManager.update_task(_id, new_task_name)

            elif command.startswith("delete"):
                _id = command[7:9]
                TaskManager.delete_task(_id)

            elif command.startswith('mark'):
                if command[4:].startswith('-in-progress'):
                    _id = command[17:]
                    TaskManager.mark_task(_id, 'in-progress')
                elif command[4:].startswith('-done'):
                    _id = command[10:]
                    TaskManager.mark_task(_id, 'done')

            elif command.startswith('quit'):
                if command == 'quit/y':
                    print("Exiting Task Manager!...")
                    break
                else:
                    res = input("Are you sure you want to quit ('Y' or 'N'): ")
                    if res.capitalize() == 'Y':
                        print("Exiting Task Manager!...")
                        break
                    else:
                        continue
        else:
            print("Not command")


running()
