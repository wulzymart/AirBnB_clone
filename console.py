#!/usr/bin/python3
"""
This module contains the class that serves as the entry point to the command
interpreter
"""
import cmd
import re
import sys


class HBNBCommand(cmd.Cmd):
    """
    Entry point into the console
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "State", "City", "Amenity",
                  "Place", "Review"]

    def do_quit(self, line):
        """Quits and exit the program"""
        print()
        return True

    def do_EOF(self, line):
        """Exits out of the program console
        """
        print()
        return True

    def emptyline(self):
        """Define the console behaviour when an empty command is
        supplied"""
        pass

    def precmd(self, line):
        """Preliminary preparations before executing command"""
        line = line.strip()
        # check wether the line is in the dot notation format
        match = re.match('\w+\.\w+\(.*\)', line)
        if match:
            args = re.findall("[\w-]+", match.group())
            # swap the command and the class name
            args[0], args[1] = args[1], args[0]
            line = " ".join(args)
            print(line) # To be removed

        if not sys.stdin.isatty() and line and line.split()[0]\
           not in ["EOF", "quit"]:
            print()
        else:
            pass

        return line

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
            return False

        arg1 = arg_list[0]
        if arg1.lower() not in type(self).class_list:
            print("** class doesn't exist **")
            return False
        # Do not forget the other functionalities

    def do_all(self, args):
        """
        Print string representation of all instances based or not on the
        class name
        """
        arg_list = args.split()
        if len(arg_list) > 1 and arg1 in type(self).class_list:
            arg1 = arg_list[0]
            # print all instances of the supplied list

        else:
            # print all instances due to NULL class name
            pass  # remove this after adding the implementation

    def do_show(self, args):
        """
        Print string representation of object based on class name
        and ID
        """
        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
            return False

        arg1 = arg_list[0]
        if arg1 not in type(self).class_list:
            print("** class doesn't exist **")
            return False

        if len(arg_list) < 2:
            print("** instance id missing **")
            return False

        arg2 = arg_list[1]
        # Add check for wether there is an object with the supplied ID
        # Do not forget to print the output if it meets all condition

    def do_delete(self, args):
        """
        Deletes an instance based on the class name and id
        """
        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
            return False

        arg1 = arg_list[0]
        if arg1 not in type(self).class_list:
            print("** class doesn't exist **")
            return False

        arg2 = arg_list[1]
        if len(arg_list) < 2:
            print("** instance id missing **")
            return False
        # Add check for wether there is an object with the supplied ID
        # Do not forget implementation to print the output if it meets
        # all condition

    def do_update(self, args):
        """Updates an instance based on the class name"""
        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
            return False

        arg1 = arg_list[0]
        if arg1 not in type(self).class_list:
            print("** class doesn't exist **")
            return False

        if len(arg_list) < 2:
            print("** instance id missing **")
            return False

        arg2 = arg_list[1]
        # Add check for wether there is an object with the supplied ID

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return False

        arg3 = arg_list[2]
        if len(arg_list) < 4:
            print("** value missing **")
            return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
