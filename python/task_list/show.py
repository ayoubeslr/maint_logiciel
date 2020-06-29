from task_list.app import TaskList
from task_list.console import Console

class Show:
    def __init__(self, console : Console):
        self.console = console

    def show(self) -> None:
        print("yoiupiiiii", TaskList(Console).tasks.items())
        
        for project, tasks in TaskList(Console).tasks.items():
            self.console.print(project)
            for task in tasks:
                self.console.print(f"  [{'x' if task.is_done() else ' '}] {task.id}: {task.description}")
            self.console.print()