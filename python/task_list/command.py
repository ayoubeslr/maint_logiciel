from task_list.app import TaskList
# import task_list.app
class Command:
    def __init__(self, command_line):
        self.command_line = command_line
    
    def command_list(self):
        command_rest = self.command_line.split(" ", 1)
        command = command_rest[0]
        print(command)
        if command == "show":
            TaskList.show()
        elif command == "add":
            TaskList.add(command_rest[1])
        elif command == "check":
            TaskList.check(command_rest[1])
        elif command == "uncheck":
            TaskList.uncheck(command_rest[1])
        elif command == "help":
            TaskList.help()
        else:
            TaskList.error(command)