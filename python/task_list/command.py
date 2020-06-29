# import task_list.app
class Command:
    def __init__(self, command_line):
        self.command_line = command_line
    
    def command_list(self):
        from task_list.app import TaskList
        from task_list.console import Console
        command_rest = self.command_line.split(" ", 1)
        command = command_rest[0]
        print("command", command)
        if command == "show":
            TaskList(Console).show()
        elif command == "add":
            TaskList(Console).add(command_rest[1])
        elif command == "check":
            TaskList(Console).check(command_rest[1])
        elif command == "uncheck":
            TaskList(Console).uncheck(command_rest[1])
        elif command == "help":
            TaskList(Console).help()
        else:
            TaskList().error(command)