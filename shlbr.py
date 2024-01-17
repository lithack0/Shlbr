#!/usr/bin/python3
import sys
def convert_linux_command(command):
    i=0
    converted_commands = [
        f"({i+1}.){command.replace(' ', '${IFS}')}",
        f"({i+2}.){command.replace('', '$@')}"
    ]

    return converted_commands

linux_command = sys.argv[1]
converted_commands = convert_linux_command(linux_command)

for converted_command in converted_commands:
    print(converted_command)
