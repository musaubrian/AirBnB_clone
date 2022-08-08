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


class HBNBCommand(cmd.Cmd):
    """
    defines the airbnb command interpretor

    args:
    Cmd - handles command input
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
        pass

    def do_EOF(self, arg):
        """
        handles EOF or ctrl+D,
        exits interpretor
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, args):
        """
        create a new instance and save it to json file
        """

        if len(args) == 0:
            print(HBNBCommand.__errors[0])
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

        except NameError:
            print(HBNBCommand.__errors[1])

    def do_update(self, args):
        """
        updates the existing instance using
        class name and id
        """
        args = shlex.split(args)
        if len(args) == 0:
            print(HBNBCommand.__errors[0])
            return
        if len(args) == 1:
            print(HBNBCommand.__errors[2])
            return
        if len(args) == 2:
            print(HBNBCommand.__errors[4])
            return
        if len(args) == 3:
            print(HBNBCommand.__errors[5])
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])()
        except NameError:
            print(HBNBCommand.__errors[1])
            return
        k = args[0] + "." + args[1]
        try:
            value = obj_dict[k]
            print(value)
        except KeyError:
            print(HBNBCommand.__errors[3])

    def do_show(self, args):
        """
        display string representaion of an instance
        using class name and id
        """

        args = shlex.split(args)
        if len(args) == 0:
            print(HBNBCommand.__errors[0])
            return
        elif len(args) == 1:
            print(HBNBCommand.__errors[2])
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])()
        except NameError:
            print(HBNBCommand.__errors[1])
            return

        k = args[0] + "." + args[1]
        k = args[0] + "." + args[1]
        try:
            val = obj_dict[k]
            print(val)
        except KeyError:
            print(HBNBCommand.__errors[3])

    def do_destroy(self, args):
        """
        deletes an instance using class name
        and id
        """

        args = shlex.split(args)
        if len(args) == 0:
            print(HBNBCommand.__errors[0])
            return
        if len(args) == 1:
            print(HBNBCommand.__errors[2])
            return

        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()

        try:
            eval(args[0])
        except NameError:
            print(HBNBCommand.__errors[1])
            return

        k = args[0] + "." + args[1]

        try:
            del (obj_dict[k])
        except KeyError:
            print(HBNBCommand.__errors[3])
            return
        storage.save()

    def do_all(self, args):
        """
         Prints all string representation
         of all instances based or not on the class name
        """
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print(HBNBCommand.__errors[1])
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(str(val))
            else:
                obj_list.append(str(val))

        print(obj_list)

    def do_count(self, args):
        '''
            Counts the number of instances.
        '''
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print(HBNBCommand.__errors[1])
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))

    def default(self, args):
        '''
            Catches all the function names that are not expicitly defined.
        '''
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except NameError:
            print("*** Unknown syntax:", args[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
