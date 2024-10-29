import cmd
import argparse
from cli.agentCommands import create_agent_command, get_agent_command, get_all_agents_command
from cli.taskCommands import TaskCommands

class MyShell(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = 'SimpleC2> '
        self.tasks = TaskCommands()
    
    def do_list_tasks(self, line):
        """List available tasks."""
        self.tasks.list_tasks()
    
    def do_get_tasks(self, line):
        parser = argparse.ArgumentParser()
        parser.add_argument('-id', required=True, help='Agent ID')
        parser.add_argument('-status', required=True, help='Task status (e.g., completed, pending)')
        
        try:
            args = parser.parse_args(line.split())
            agent_id = args.id
            status = args.status
            
            if status != "completed" and status != "pending" and status != "all":
                print("Status must be completed or pending or all")
                return
            
            self.tasks.get_tasks(agent_id, status)
        
        except SystemExit:
            print("Error parsing arguments for get_tasks function")
    
    def do_select_task(self, line):
        """Select a task to execute. Usage: select_task <task_name> <agentId> [args]"""
        parser = argparse.ArgumentParser()
        parser.add_argument('-task', required=True, help='Task name (e.g., shell, screenshot)')
        parser.add_argument('-id', required=True, help='Agent ID')
        parser.add_argument('-priority', required=True, help='Priority level (e.g., low, medium, high)')
        parser.add_argument('-command', nargs='+', help='Command for the shell task, capture multiple arguments')
        
        try:
            args = parser.parse_args(line.split())
            task_name = args.task
            agent_id = args.id
            priority = args.priority
            command_args = args.command if args.command else []
            
            if priority != "high" and priority != "low":
                print("Priority must be high or low")
                return

            # Execute the task with agentId and optional arguments
            self.tasks.execute_task(task_name, agent_id, priority, command_args)

        except SystemExit as e:
            print("Error parsing arguments for select_task function\n")
        
    def do_get_all_agents(self, line):
        try:
            get_all_agents_command()
        except SystemExit:
            print("Error getting all agents") 
        
    
    def do_create_agent(self, line):
        
        """Manage agents. Example: agent create AGENT123 --os 'Linux'"""
        
        parser = argparse.ArgumentParser(prog='create_agent', description="Create a new agent")
        parser.add_argument('agentId', type=str, help="Name of the agent, pass random for a random name")
        
        try:
            args = parser.parse_args(line.split())
            create_agent_command(args)
        except SystemExit:
            print("Error parsing arguments for create_agent function")
        
    def do_get_agent(self, line):
        parser = argparse.ArgumentParser(prog='get_agent', description="Get an agent")
        parser.add_argument('agentId', type=str, help="Name of the agent")
        
        try:
            args = parser.parse_args(line.split())
            get_agent_command(args)
        
        except SystemExit:
            print("Error parsing arguments for get_agent function")
 
    def help_add(self, line):
        print("Help Agent")
        
        
    def do_exit(self, line):
        """Exit the CLI shell."""
        
        print("Exiting...")
        return True
    
    def do_help(self, line):
        print("*******Help menu*********")
        print("create_agent <name>: to create an agent with a name.")
        print("get_agent <name>: to get an agent with the name.")
        print("get_all_agents: to get all agents.")
        print("list_tasks: to list all available tasks.")
        print("get_tasks -id <agentId> -status <status>: to get tasks for a specific agent.")
        print("select_task -task <task_name> -id <agentId> -priority <priority> -command <args>: to select a task to execute.")