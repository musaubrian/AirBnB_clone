#!/usr/bin/env python3
"""console to handle the commands to be used"""
import cmd
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Reviews
from models.state import State
from models.user import User


class HBNBcommand(cmd.Cmd):
    """
    handle the commands
    """

    prompt = "(hbnb) "
    __errors = [
            "** class name missing **",
            "** class doesn't exist **",
            "** instance id missing **",
            "** no instance found **",
            "** attribute name missing **",
            "** value missing **"
            ]

    def do_emptyline(self):
        """
        handles an empty line,
        keeps prompt alive
        """
        return False

    def do_EOF(self, arg):
        """
        handles EOF or ctrl+D,
        exits interpretor
        """
        print()
        return True

    def do_quit(self, arg):
        """
        handles `quit` command,
        exits the interpretor
        """
        return True

    def do_create(self, args):
        """
        create a new instance and save it to json file
        """

        if len(args) == 0:
            print(HBNBcommand.__errors[0])
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

        except NameError:
            print(HBNBcommand.__errors[1])

    def do_update(self, args):
        """
        updates the existing instance using
        class name and id
        """
        args = shlex.split(args)
        if len(args) == 0:
            print(HBNBcommand.__errors[0])
            return
        if len(args) == 1:
            print(HBNBcommand.__errors[2])
            return
        if len(args) == 2:
            print(HBNBcommand.__errors[4])
            return
        if len(args) == 3:
            print(HBNBcommand.__errors[5])
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:        
            eval(args[0])()
        except NameError:
            print(HBNBcommand.__errors[1])
            return
        k = args[0] + "." + args[1]
        try:
            value = obj_dict[k]
            print(value)
        except KeyError:
            print(HBNBcommand.__errors[3])

    def do_show(self, args):
        """
        display string representaion of an instance
        using class name and id
        """

        args = shlex.split(args)
        if len(args) == 0:
            print(HBNBcommand.__errors[0])
        elif len(args) == 1:
            print(HBNBcommand.__errors[2])
            return
        storage  = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print(HBNBcommand.__errors[1])
            return

        k = f"{args[0]} . {args[1]}"
        k = f"{args[0]} . {args[1]}"

        try:
            print(obj_dict[k])
        except KeyError:
            print(HBNBcommand.__errors[3])


if __name__ == "__main__":
    """starting point for the cmd loop"""
    HBNBcommand().cmdloop()
