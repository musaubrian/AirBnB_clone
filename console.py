#!/usr/bin/env python3
"""console to handle the commands to be used"""
import cmd


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


if __name__ == "__main__":
    """starting point fo the cmd loop"""
    HBNBcommand().cmdloop()
