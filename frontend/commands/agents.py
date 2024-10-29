from bson.objectid import ObjectId
import requests
import json
from utils.jsonTools import list_all_json

class AgentModel:
    def __init__(self, SECRET_API):
        self.SECRET_API = SECRET_API
        
    def get_all_agents(self):
        headers = {
            'x-api-key': self.SECRET_API,
            'Content-Type': 'application/json'
        }
        
        response = requests.get('http://localhost:2000/api/agents/get-all-agents', headers=headers)
        
        if response.status_code == 200:
            return response.json()

        else:
            return "Error getting all agents: " + response.json().get('message', 'No message provided')

    def create_agent(self, agent_id):
        headers = {
            'x-api-key': self.SECRET_API,
            'Content-Type': 'application/json'
        }
        
        payload = {
            "agentId": str(agent_id)
        }
        
        response = requests.post("http://localhost:2000/api/agents/create-agent", headers=headers, json=payload)

        
        if response.status_code == 201:
            return "Agent created successfully"
        else:
            return "Error creating agent: " + response.json().get('message', 'No message provided')
    
    
    
    def get_agent(self, agent_id):
        
        headers = {
            'x-api-key': self.SECRET_API,
            'Content-Type': 'application/json'
        }
        
        payload = {
            "agentId": str(agent_id)
        }
        
        response = requests.get("http://localhost:2000/api/agents/get-agent", headers=headers, json=payload)
    
        
        if response.status_code == 200:
            return response.json()
        else:
            return "Error creating agent: " + response.json().get('message', 'No message provided')
    