from commands.tasks import run_shell, take_screenshot, upload_file, get_tasks
from utils.misc import print_tasks

class TaskCommands:
    """Class to manage task commands."""

    def __init__(self):
        self.tasks = {
            'shell': (run_shell, 'Execute shell commands with arguments'),
            'screenshot': (take_screenshot, 'Take a screenshot'),
            'upload': (upload_file, 'Upload a file'),
        }

    def list_tasks(self):
        """List available tasks."""
        print("Available tasks:")
        for task_name, (_, description) in self.tasks.items():
            print(f"- {task_name}: {description}")
    
    def get_tasks(self, agent_id, status):
        """Get tasks for a specific agent."""
        pretty_tasks = get_tasks(agent_id, status)
        print_tasks(pretty_tasks)
        

    def execute_task(self, task_name, agent_id, priority, task_args):
        """Execute the selected task with agentId and arguments."""
        if task_name in self.tasks:
            
            # Check if the task requires agentId and arguments
            if task_name == 'shell':
                if len(task_args) == 0:
                    print("Please provide a command to run with the shell task")
                    return
                print(f"Executing task: {task_name} for agentId: {agent_id} with arguments: {task_args}")

                self.tasks[task_name][0](agent_id, priority, task_args)  # Pass agentId and args to shell
            else:
                print(f"Executing task: {task_name} for agentId: {agent_id} with arguments: {task_args}")

                self.tasks[task_name][0](agent_id, priority)  # Pass only agentId for other tasks
        else:
            print(f"Task '{task_name}' not found. Type 'list_tasks' to see available tasks.")