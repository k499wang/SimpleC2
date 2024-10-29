# SimpleC2

SimpleC2 is a lightweight Command and Control (C2) server built with Mongo, Express and Python for the backend and c++ for the client.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/SimpleC2.git
    ```
2. Navigate to the project directory:
    ```sh
    cd SimpleC2
    ```
3. Install dependencies:
    ```sh
    npm install
    ```
4. Install the following python packages
    ```
    pip install requests
    ```

## Usage

1. Start the server:
    ```sh
    npm server start
    ```
2. Run the CLI
    ```python
    python3 main.py
    ```

## Configuration

Edit the `.env` file to customize settings such as server port, encryption keys, and more.

It should look like the following

    ```
    PORT=2000
    MONGO_URI=mongodb://localhost:27017/DATABASE
    DATABASE_NAME=DATABASE
    SECRET_API_KEY=secret
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact k499wang@uwaterloo.ca.
