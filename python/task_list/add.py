from task_list.app import TaskList
from task_list.console import Console
from task_list.task import Task

class Add:
    def __init__(self, console : Console):
        self.console = console

    def add(self, command_line: str) -> None:
        sub_command_rest = command_line.split(" ", 1)
        sub_command = sub_command_rest[0]

        if sub_command == "project":
            print('projet')
            self.add_project(sub_command_rest[1])

        elif sub_command == "task":
            print('tasl')
            project_task = sub_command_rest[1].split(" ", 1)
            print(project_task)
            self.add_task(project_task[0], project_task[1])
        else:
            self.error(command)
    
    def add_task(self, project: str, description: str) -> None:
        project_tasks = TaskList(Console).tasks.get(project)
        if project_tasks is None:
            # self.console.print(f"Could not find a project with the name {project}.")
            # self.console.print()
            print(f"Could not find a project with the name {project}.")
            print()
            return
        project_tasks.append(Task(self.next_id(), description, False))
    
    def add_project(self, name: str) -> None:
        TaskList(Console).tasks[name] = []
