from commands.agents import AgentModel
from utils.misc import generate_random_string, print_agent_ids
import json
from dotenv import load_dotenv
import os


load_dotenv()

SECRET_API = os.getenv("SECRET_API_KEY")

if not SECRET_API:
    raise ValueError("SECRET_API environment variable not set")

def get_all_agents_command():
    agent = AgentModel(SECRET_API)
    response = agent.get_all_agents()
    print_agent_ids(response)
    

def create_agent_command(args):
    agent_id = args.agentId
    
    if(agent_id == "random"):
        print("\nGenerating random agent id... ")
        agent_id = generate_random_string()
        print("Agent id: " + agent_id)
        print("\n")
    
    
    agent = AgentModel(SECRET_API)
    response = agent.create_agent(agent_id)
    print(response)
    
def get_agent_command(args):
    agent_id = args.agentId
    agent = AgentModel(SECRET_API)
    response = agent.get_agent(agent_id)
    
    print("\n*** Agent ***")
    print(json.dumps(response, indent=4, default=str))
    print("*** Agent End ***\n")