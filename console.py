#!/usr/bin/python3
"""
This module contains the class that serves as the entry point to the command
interpreter
"""
import cmd
import re
import sys
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Entry point into the console
    """
    prompt = "(hbnb) "
    class_list = {"BaseModel": BaseModel, "User": User,
                  "State": State, "City": City,
                  "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def do_quit(self, line):
        """Quits and exit the program"""
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
        match = re.match(r'\w+\.\w+\(.*\)', line)
        if match:
            # search line and split the dot.notation line into arg1.arg2(arg3)
            args = re.search(r"([\w]+)\.([\w]+)\((.*?)\)",
                             match.group()).groups()
            args = list(args)
            # swap the command and the class name
            args[0], args[1] = args[1], args[0]
            in_brak = args[2]  # match characters in bracket
            if in_brak:
                args = args[:2] + re.findall(r'"?([\w\s-]+)"?', in_brak)
                args = ['"' + i + '"' if len(i.split()) > 1 else i.strip()
                        for i in args if not i.isspace()]
            line = " ".join(args)

        if not sys.stdin.isatty() and line and line.split()[0] not in ["EOF"]:
            print()
        else:
            pass

        return line

    def do_count(self, args):
        """Count the number of instances in the storage system"""
        arg_list = args.split()
        all_objs = storage.all()
        storage.reload()
        if arg_list and arg_list[0] in type(self).class_list:
            arg1 = arg_list[0]
            cls_name = arg_list[0]
            print(len([str(v) for k, v in all_objs.items() if
                       k.startswith(cls_name)]))
        else:
            print(len([str(i) for i in all_objs.values()]))

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
            return False

        arg1 = arg_list[0]
        if arg1 not in type(self).class_list:
            print("** class doesn't exist **")
            return False
        obj = type(self).class_list[arg_list[0]]()
        storage.new(obj)
        obj.save()
        storage.reload()
        print(obj.id)

    def do_all(self, args):
        """
        Print string representation of all instances based or not on
        the class name
        """
        arg_list = args.split()
        all_objs = storage.all()
        storage.reload()
        if arg_list and arg_list[0] in type(self).class_list:
            arg1 = arg_list[0]
            cls_name = arg_list[0]
            print([str(v) for k, v in all_objs.items() if
                   k.startswith(cls_name)])
        else:
            print([str(i) for i in all_objs.values()])

    def do_show(self, args):
        """
        Print string representation of object based on class name
        and ID
        """
        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
            return False

        class_name = arg_list[0]
        if class_name not in type(self).class_list:
            print("** class doesn't exist **")
            return False

        if len(arg_list) < 2:
            print("** instance id missing **")
            return False

        id = arg_list[1]
        key = ".".join([class_name, id])
        storage.reload()
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
            return False
        class_name = arg_list[0]
        if class_name not in type(self).class_list:
            print("** class doesn't exist **")
            return False

        if len(arg_list) < 2:
            print("** instance id missing **")
            return False
        id = arg_list[1]

        key = ".".join([class_name, id])
        storage.reload()
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return False
        del storage.all()[key]
        storage.save()
        storage.reload()

    def do_update(self, args):
        """Updates an instance based on the class name"""
        arg_list = re.findall(r'"[^"]*"|\S+', args)
        if len(arg_list) < 1:
            print("** class name missing **")
            return False
        class_name = arg_list[0]

        if class_name not in type(self).class_list:
            print("** class doesn't exist **")
            return False

        if len(arg_list) < 2:
            print("** instance id missing **")
            return False
        id = arg_list[1]

        key = ".".join([class_name, id])
        storage.reload()
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return False
        obj = all_objs[key]

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return False

        for attr_idx in range(2, len(arg_list), 2):
            try:
                setattr(obj, arg_list[attr_idx].strip('"'),
                        arg_list[attr_idx + 1].strip('"'))
            except IndexError as ie:
                print("** value missing **")
                return False
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
