#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand class - entry point of the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
            Exit the command interpreter
        """
        return True

    def do_EOF(self, arg):
        """
            Exit the command interpreter when end-of-file is reached
        """
        print()
        return True

    def emptyline(self):
        """
            Do nothing on empty line + ENTER
        """
        pass

    def do_create(self, arg):
        """
            Create a new instance of BaseModel, save it to the JSON file,
            and print the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Print the string representation of an instance based on the
            class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.all().pop(key)
        storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances based or not
            on the class name
        """
        args = arg.split()
        objs = []
        if len(args) == 0:
            objs = list(storage.all().values())
        elif args[0] in storage.classes:
            objs = [v for k, v in storage.all().items()
                    if args[0] in k]
        else:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objs])

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file)
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
 key = "{}.{}".format(args[0], args[1])
    if key not in storage.all():
        print("** no instance found **")
        return
    obj = storage.all()[key]
    if len(args) == 2:
        print("** attribute name missing **")
        return
    if len(args) == 3:
        print("** value missing **")
        return
    attr_name = args[2]
    attr_value = args[3]
    if hasattr(obj, attr_name):
        attr_type = type(getattr(obj, attr_name))
        attr_value = attr_type(attr_value)
        setattr(obj, attr_name, attr_value)
        obj.save()
    else:
        setattr(obj, attr_name, attr_value)
        obj.save()

def default(self, arg):
    """ Called on an input line when the command prefix is not recognized.
    If the line starts with a class name followed by a dot, it will be
    interpreted as a command to show, create, destroy or update an instance
    of that class.
    """
    args = arg.split(".")
    if len(args) < 2:
        cmd.Cmd.default(self, arg)
        return
    class_name = args[0]
    if class_name not in storage.classes:
        print("** class doesn't exist **")
        return
    if args[1] == "all()":
        self.do_all(class_name)
        return
    if args[1] == "count()":
        self.do_count(class_name)
        return
    if not args[1].startswith("show(") and \
            not args[1].startswith("destroy(") and \
            not args[1].startswith("update("):
        cmd.Cmd.default(self, arg)
        return
    obj_id = args[1][args[1].find("(")+2:args[1].find(")")]
    if len(obj_id) == 0:
        print("** instance id missing **")
        return
    if obj_id.isnumeric():
        obj_id = int(obj_id)
    else:
        obj_id = str(obj_id)
    key = "{}.{}".format(class_name, obj_id)
    if key not in storage.all():
        print("** no instance found **")
        return
    obj = storage.all()[key]
    if args[1].startswith("show("):
        print(obj)
    elif args[1].startswith("destroy("):
        storage.delete(obj)
        storage.save()
    elif args[1].startswith("update("):
        update_args = args[1][args[1].find("(")+1:-1]
        if len(update_args) == 0:
            return
        update_args = update_args.split(",")
        for i, arg in enumerate(update_args):
            update_args[i] = arg.strip()
        if len(update_args) < 2:
            return
        attr_name = update_args[0]
        attr_value = update_args[1]
        if len(update_args) == 2:
            return
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]
        if len(update_args) > 2:
            if attr_value.isnumeric():
                attr_value = int(attr_value)
            else:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass
        setattr(obj, attr_name, attr_value)
        obj.save()
if __name__ == "__main__":
    HBNBCommand().cmdloop()
