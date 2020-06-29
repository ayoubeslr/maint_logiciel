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
        self.console.print("Commands:")
        self.console.print("  show")
        self.console.print("  add project <project name>")
        self.console.print("  add task <project name> <task description>")
        self.console.print("  check <task ID>")
        self.console.print("  uncheck <task ID>")
        self.console.print()
        # msg = ["Commands:", "  show", "  add project <project name>", "  add task <project name> <task description>", "  check <task ID>", "  uncheck <task ID>", ""]
        # for elt in msg :
        #     self.console.print(elt)

    def error(self, command: str) -> None:
        self.console.print(f"I don't know what the command {command} is.")
        self.console.print()

    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id
