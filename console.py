#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    """
    This is the text displyed by the prompt
    """
    def do_EOF(self, args):
        """
        This is the End of File command which when entered is used to exit the shell. 
        It includes Crontol-D on Unix and Control Z on Windows operating system.
        """
        return True
    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True
    def emptyline(self):
        """
        This a method called an empty line is entered by the user
        """
        pass
    def default(self, args):
        """
        This method is called when undocumented commands are entered
        """
        print(f"Unkonwn command: {args}")
if __name__ == '__main__':
    """
    creates an instance the cmd subclass and then runs the cmdloop method
    """
    HBNBCommand().cmdloop()

