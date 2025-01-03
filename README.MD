# SimpleC2

**SimpleC2** is a lightweight Command and Control (C2) server built with MongoDB, Express, and Python for the backend, and C++ for the client. This project aims to provide an efficient and flexible framework for managing and controlling client applications.

Check the implant code here: [C2ImplantSrc](https://github.com/k499wang/C2ImplantSrc).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Requirements](#requirements)

## Installation

Follow these steps to set up the SimpleC2 server:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/SimpleC2.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd SimpleC2
    ```

3. **Install Node.js dependencies**:
    ```sh
    npm install
    ```

4. **Install required Python packages**:
    ```sh
    pip install requests
    ```

5. **Set up MongoDB**:
   - Ensure you have a local MongoDB instance running. You can download MongoDB from [mongodb.com](https://www.mongodb.com/try/download/community) and follow the installation instructions.
   - Start your MongoDB server:
     ```sh
     mongod
     ```

## Usage

*Note*: You must start the server before trying to run the CLI.

1. **Start the server**:
    ```sh
    npm run start
    ```

2. **Run the CLI**:
    ```python
    python3 main.py

    SimpleC2 >
    ```

## 🖥️ Command-Line Interface (CLI) for Agent Management

This project includes a simple command-line interface (CLI) for managing agents, tasks, and interacting with the C2 server. The CLI is built using Python's `cmd` module and allows administrators to easily control and interact with agents deployed on different systems.

### Features

- **Agent Management**: Create, retrieve, and list agents in the system.
- **Task Management**: List available tasks, view tasks for specific agents, and execute tasks on agents.
- **Task Execution**: Select a task and execute it with optional arguments on a specific agent.

### CLI Commands

The following commands are available in the CLI shell:

#### `create_agent <agentId>`
Creates a new agent with the specified agent ID. If `agentId` is set to "random", a random agent name will be generated.

**Example**:  
`create_agent AGENT123`

#### `get_agent <agentId>`
Retrieves the details of an agent by its agent ID.

**Example**:  
`get_agent AGENT123`

#### `get_all_agents`
Lists all agents currently available in the system.

**Example**:  
`get_all_agents`

#### `list_tasks`
Lists all available tasks in the system that can be executed on agents.

**Example**:  
`list_tasks`

#### `get_tasks -id <agentId> -status <status>`
Retrieves a list of tasks for a specific agent, filtered by task status. Valid status values are:
- `completed`
- `pending`
- `all` (default)

**Example**:  
`get_tasks -id AGENT123 -status pending`

#### `select_task -task <task_name> -id <agentId> -command <args>`
Selects a task to execute on an agent. You can specify the task name, agent ID, and optional command arguments (e.g., a shell command or additional parameters).

**Example**:  
`select_task -task shell -id AGENT123 -command "ls -la"`

#### `exit`
Exits the CLI shell.

**Example**:  
`exit`

### Usage Example

1. **Create an Agent**:  
   To create a new agent with ID `AGENT123`, use the following command:  
   `create_agent AGENT123`

2. **List Available Tasks**:  
   To list all available tasks, use:  
   `list_tasks`

3. **Get Tasks for a Specific Agent**:  
   To get the pending tasks for agent `AGENT123`, run:  
   `get_tasks -id AGENT123 -status pending`

4. **Select and Execute a Task**:  
   To select and execute the `shell` task with a command (`ls -la`) on agent `AGENT123`, use:  
   `select_task -task shell -id AGENT123 -command "ls -la"`

5. **Exit the CLI**:  
   To exit the shell, simply type:  
   `exit`

### Notes

- The CLI supports a wide range of commands to manage agents and execute tasks.
- Arguments for each command are flexible and can be adjusted to meet your needs (e.g., different agent IDs, task names, or command arguments).
- If you need help or further guidance, use the `help` command within the CLI for detailed usage instructions:  
  `help`

## Configuration

Edit the `.env` file to customize settings such as server port, encryption keys, and MongoDB connection details. Your `.env` file should look like this:

```
PORT=2000 MONGO_URI=mongodb://localhost:27017/DATABASE 
DATABASE_NAME=DATABASE
SECRET_API_KEY=secret
```

Ensure that `DATABASE` is replaced with your desired database name.

## Requirements

- **Node.js**: Ensure you have Node.js installed (version 12 or later).
- **Python**: Python 3.x is required.
- **MongoDB**: A local instance of MongoDB must be running.

## Troubleshooting

- **MongoDB Connection Issues**:
  - Ensure MongoDB is running: Check if the MongoDB service is active with `systemctl status mongod` or by connecting via the MongoDB shell.
  
- **Server Not Starting**:
  - Ensure you have installed all dependencies correctly. Run `npm install` again to confirm.
  - Check the server logs for any error messages that may indicate what went wrong.

- **Invalid Command Errors**:
  - Make sure the command format is correct and that the client ID matches an existing client in the database.
