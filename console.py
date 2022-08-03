#!/usr/bin/env python3
"""console to handle the commands to be used"""
import cmd

class HBNBcommand(cmd.Cmd):
    """
    handle the commands
    """

    prompt = "(hbnb) "


if __name__ == "__main__":
    """starting point fo the cmd loop"""
    HBNBcommand().cmdloop()
