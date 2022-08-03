#!/usr/bin/env python3
"""console to handle the commands to be used"""
import cmd

class HBNBcommand(cmd.Cmd):
    """
    handle the commands
    """

    prompt = "(hbnb) "

    def do_emptyline(self):
        """handles an empty line"""
        return False

    def do_EOF(self, arg):
        """handles EOF or ctrl+D"""
        return True


if __name__ == "__main__":
    """starting point fo the cmd loop"""
    HBNBcommand().cmdloop()
