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
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        updates the existing instance using
        class name and id
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")



if __name__ == "__main__":
    """starting point for the cmd loop"""
    HBNBcommand().cmdloop()
