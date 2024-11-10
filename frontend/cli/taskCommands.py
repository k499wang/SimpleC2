from commands.tasks import run_shell, persistence, kill, get_task
from utils.misc import print_tasks

class TaskCommands:
    """Class to manage task commands."""

    def __init__(self):
        self.tasks = {
            'shell': (run_shell, 'Execute shell commands with arguments'),
            'persistence': (persistence, 'Installs persistence via Registry Keys'),
            "kill": (kill, "kills the agent")
        }

    def list_tasks(self):
        """List available tasks."""
        print("\nAvailable tasks:")
        for task_name, (_, description) in self.tasks.items():
            print(f"- {task_name}: {description}")
        
        print("\n")
    
    def get_tasks(self, agent_id, status):
        """Get tasks for a specific agent."""
        pretty_tasks = get_task(agent_id, status)
        print_tasks(pretty_tasks)
        

    def execute_task(self, task_name, agent_id, task_args):
        """Execute the selected task with agentId and arguments."""
        if task_name in self.tasks:
            # Check if the task requires agentId and arguments
            if task_name == 'shell':
                if len(task_args) == 0:
                    print("Please provide a command to run with the shell task")
                    return
                print(f"\nExecuting task: {task_name} for agentId: {agent_id} with arguments: {task_args}\n")

                self.tasks[task_name][0](agent_id, task_args)  # Pass agentId and args to shell
            else:
                print(f"\nExecuting task: {task_name} for agentId: {agent_id} with arguments: {task_args}\n")

                self.tasks[task_name][0](agent_id)  # Pass only agentId for other tasks
        else:
            print(f"\nTask '{task_name}' not found. Type 'list_tasks' to see available tasks.\n")