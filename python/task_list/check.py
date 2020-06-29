from task_list.app import TaskList
from task_list.console import Console
from task_list.task import Task

class Check:
    def __init__(self, console : Console):
        self.console = console
    
    def set_done(self, id_string: str, done: bool) -> None:
        id_ = int(id_string)
        for project, tasks in TaskList(Console).tasks.items()):
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    return
        # self.console.print(f"Could not find a task with an ID of {id_}")
        # self.console.print()
        print(f"Could not find a task with an ID of {id_}")
        print()


    def check(self, id_string: str) -> None:
        self.set_done(id_string, True)

    def uncheck(self, id_string: str) -> None:
        self.set_done(id_string, False)

