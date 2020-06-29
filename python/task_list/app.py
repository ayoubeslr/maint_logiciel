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

    def help(self) -> None:
        print("Commands:")
        print("  show")
        print("  add project <project name>")
        print("  add task <project name> <task description>")
        print("  check <task ID>")
        print("  uncheck <task ID>")
        print()

    def error(self, command: str) -> None:
        print(f"I don't know what the command {command} is.")
        print()

