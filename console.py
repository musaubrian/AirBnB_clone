#!/usr/bin/env python3
"""console to handle the commands to be used"""
import cmd

<<<<<<< HEAD

=======
>>>>>>> 69b38dbe836d229bfe3606c23c91882d4120ec0e
class HBNBcommand(cmd.Cmd):
    """
    handle the commands
    """

    prompt = "(hbnb) "

    def do_emptyline(self):
<<<<<<< HEAD
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
        return True

    def do_quit(self, arg):
        """
        handles `quit` command,
        exits the interpretor
        """
=======
        """handles an empty line"""
        return False

    def do_EOF(self, arg):
        """handles EOF or ctrl+D"""
>>>>>>> 69b38dbe836d229bfe3606c23c91882d4120ec0e
        return True


if __name__ == "__main__":
    """starting point fo the cmd loop"""
    HBNBcommand().cmdloop()
