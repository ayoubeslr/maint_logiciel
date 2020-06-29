from typing import Dict, List

from task_list.console import Console
from task_list.task import Task



class TaskList:
    QUIT = "quit"

    def __init__(self, console : Console) -> None:
        self.console = console
        self.last_id: int = 0
        self.tasks: Dict[str, List[Task]] = dict()

    def run(self) -> None:
        while True:
            command = self.console.input("> ")
            if command == self.QUIT:
                break
            self.execute(command)

    def execute(self, command_line: str ) -> None:
        from task_list.command import Command
        command = Command(command_line)
        command.command_list()

    def show(self) -> None:
        for project, tasks in self.tasks.items():
            self.console.print(project)
            for task in tasks:
                self.console.print(f"  [{'x' if task.is_done() else ' '}] {task.id}: {task.description}")
            self.console.print()

    def add(self, command_line: str) -> None:
        sub_command_rest = command_line.split(" ", 1)
        sub_command = sub_command_rest[0]
        if sub_command == "project":
            self.add_project(sub_command_rest[1])
        elif sub_command == "task":
            project_task = sub_command_rest[1].split(" ", 1)
            self.add_t:ask(project_task[0], project_task[1])
        else:
            self.error(command)

    def add_project(self, name: str) -> None:
        self.tasks[name] = []

    def add_task(self, project: str, description: str) -> None:
        project_tasks = self.tasks.get(project)
        if project_tasks is None:
            self.console.print(f"Could not find a project with the name {project}.")
            self.console.print()
            return
        project_tasks.append(Task(self.next_id(), description, False))

    def check(self, id_string: str) -> None:
        self.set_done(id_string, True)

    def uncheck(self, id_string: str) -> None:
        self.set_done(id_string, False)

    def set_done(self, id_string: str, done: bool) -> None:
        id_ = int(id_string)
        for project, tasks in self.tasks.items():
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    return
        self.console.print(f"Could not find a task with an ID of {id_}")
        self.console.print()

    def help(self) -> None:
        msg = ["Commands:", "  show", "  add project <project name>", "  add task <project name> <task description>", "  check <task ID>", "  uncheck <task ID>", ""]
        for elt in msg :
            self.console.print(elt)

    def error(self, command: str) -> None:
        self.console.print(f"I don't know what the command {command} is.")
        self.console.print()

    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id
