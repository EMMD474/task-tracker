# Task-Tracker CLI

This is a simple task tracker that keeps track of all tasks. Tasks are categorized as:

1. **todo**
2. **in-progress**
3. **done**

Tasks can be **added**, **updated**, and **deleted**.

## Features

- Add new tasks with a description.
- Update existing tasks.
- Delete tasks.
- Mark tasks as **in-progress** or **done**.
- List all tasks.
- List tasks by their status (**todo**, **in-progress**, **done**).

## Requirements

- Python 3.x
- No external libraries required.

## Installation

Clone the repository:

```commandline
git clone https://github.com/EMMD474/task-tracker.git
```

Navigate to the project directory:

```commandline
cd task-tracker
```

## Running the Program

Run the CLI application:

```commandline
python main.py
```

### Example Commands

- Add a task:
  ```commandline
  python main.py add "Task name"
  ```
- Update a task:
  ```commandline
  python main.py update 1 "Updated task name"
  ```
- Delete a task:
  ```commandline
  python main.py delete 1
  ```
- List all tasks:
  ```commandline
  python main.py list
  ```
- List tasks by status:
  ```commandline
  python main.py list in-progress
  ```

## Data Storage

Tasks are stored in a `tasks.json` file in the root directory. If the file does not exist, it will be created automatically.

## Error Handling

- Invalid commands or arguments are gracefully handled.
- The program ensures data integrity even during abrupt interruptions.

## Link to Project Challenge:

> [Task Tracker on roadmap.sh](https://roadmap.sh/projects/task-tracker)

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to fork the repository, open issues, or submit pull requests to enhance the project.

## Author

**Emmanuel Banda**

For any questions or suggestions, please reach out at [emmanueldaliso3@gmail.com](mailto:emmanueldaliso3@gmail.com).
