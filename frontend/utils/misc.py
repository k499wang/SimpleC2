        
import random
import string

def print_agent_ids(agents):
    for agent in agents:
        print(f"AgentId: {agent['agentId']}")

def print_tasks(tasks):
    for task in tasks:
        if task['arguments'] == None or task['arguments'] == "":    
            task['arguments'] = "No Arguments specified"
            
        print(f"AgentId: {task['agentId']}, Command: {task['command']}, Args: {task['arguments']}, Priority: {task['priority']}, Status: {task['status']}")

def generate_random_string(length=8):
    letters = string.ascii_letters
    str = ''
    for i in range(length):
        str += random.choice(letters)
    
    return str