import requests
from utils.jsonTools import list_all_json
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_API = os.getenv("SECRET_API_KEY")

def run_shell(agent_id, args):
    """Logic to execute shell commands with arguments for a specific agent."""
    command = ' '.join(args)  # Join the arguments to form the command string
    print(f"Running shell command for agentId {agent_id}: {command}" )
    
    headers = {
            'x-api-key': SECRET_API,
            'Content-Type': 'application/json'
    }
    
    newArgs = ' '.join(args)
    
    payload = {
        "agentId": agent_id,
        "command": "shell",
        "args": newArgs,
    }
    
    response = requests.post('http://localhost:2000/api/tasks/createTasks', headers=headers, json=payload)
    
    if response.status_code == 201:
        print(response.json())
    else:
        print( "Error running shell command: " + response.json().get('message', 'No message provided'))
    
def get_task(agent_id, status):
    """Logic to get tasks for a specific agent."""
    print(f"Getting tasks for agentId {agent_id} with status {status}")
    
    headers = {
            'x-api-key': SECRET_API,
    }
    
    params = {
        "agentId": agent_id,
        "status": status
    }
    
    response = requests.get('http://localhost:2000/api/tasks/getTasks', headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return "Error getting tasks: " + response.json().get('message', 'No message provided')


def kill(agent_id):
    headers = {
            'x-api-key': SECRET_API,
    }
    
    payload = {
        "agentId": agent_id,
        "command": "kill"
    }
    
    response = requests.post('http://localhost:2000/api/tasks/createTasks', headers=headers, json=payload)
    
    if response.status_code == 201:
        print(response.json())
    else:
        print( "Error killing agent: " + response.json().get('message', 'No message provided'))
    
    

def persistence(agent_id):
    print(f"Persistence for {agent_id}")
    
    headers = {
            'x-api-key': SECRET_API,
    }
    
    payload = {
        "agentId": agent_id,
        "command": "persistence"
    }
    
    response = requests.post('http://localhost:2000/api/tasks/createTasks', headers=headers, json=payload)
    
    if response.status_code == 201:
        print(response.json())
    else:
        print( "Error persisting " + response.json().get('message', 'No message provided'))
