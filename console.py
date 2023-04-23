#!/usr/bin/python3
"""The console module for the AirBnB clone project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Custom command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program gracefully"""
        print()
        return True

    def emptyline(self):
        """Do nothing when the user inputs an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
