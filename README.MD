# SimpleC2

**SimpleC2** is a lightweight Command and Control (C2) server built with MongoDB, Express, and Python for the backend, and C++ for the client. This project aims to provide an efficient and flexible framework for managing and controlling client applications.

Check the implant code here: [C2ImplantSrc](https://github.com/k499wang/C2ImplantSrc).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Requirements](#requirements)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

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

1. **Start the server**:
    ```sh
    npm run start
    ```

2. **Run the CLI**:
    ```python
    python3 main.py
    ```

3. **Access the server**:
   - By default, the server runs on `http://localhost:2000`. You can access it through a web browser or use API testing tools like Postman.

### Example Commands

- **Sending a command to a client**:
    ```json
    POST http://localhost:2000/command
    {
        "client_id": "YOUR_CLIENT_ID",
        "command": "YOUR_COMMAND"
    }
    ```

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
