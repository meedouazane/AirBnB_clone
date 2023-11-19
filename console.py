#!/usr/bin/env python3
''' command interpreter '''
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    ''' contains the entry point of the command interpreter '''

    prompt = "(hbnb) "
    class_names = [
        "User",
        "Place",
        "City",
        "Amenity",
        "Review",
        "State",
        "BaseModel"
        ]

    def do_EOF(self, line):
        ''' end of file '''
        return True

    def do_create(self, line):
        '''  Creates a new instance of class '''
        command = line.split()
        if len(command) < 1:
            print("** class name missing **")
        elif command[0] in HBNBCommand().class_names:
            full_class_name = eval(command[0] + "()")
            new_instance = full_class_name
            models.storage.save()
            print(f"{new_instance.id}")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        ''' Prints the string representation of an instance '''
        command = line.split()
        obj = models.storage.all()
        if len(command) == 0:
            print("** class name missing **")
        elif len(command) == 1:
            if command[0] in HBNBCommand().class_names:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            key = command[0] + '.' + command[1]
            if key in obj:
                print(obj[key])
            else:
                if command[0] in HBNBCommand().class_names:
                    print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        ''' Deletes an instance based on the class name and id '''
        command = line.split()
        obj = models.storage.all()
        if len(command) == 0:
            print("** class name missing **")
        elif len(command) == 1:
            if command[0] in HBNBCommand().class_names:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            key = command[0] + '.' + command[1]
            if key in obj:
                del obj[key]
                models.storage.save()
            else:
                if command[0] in HBNBCommand().class_names:
                    print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_update(self, line):
        '''  Updates an instance based on the class name and id '''
        command = line.split()
        obj = models.storage.all()
        if len(command) == 0:
            print("** class name missing **")
        elif len(command) == 1:
            if command[0] in HBNBCommand().class_names:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(command) == 2:
            for items in obj.values():
                key = command[0] + '.' + command[1]
                if key in obj:
                    print("** attribute name missing **")
                    break
                else:
                    print("** no instance found **")
                    break
        elif len(command) == 3:
            print("** value missing **")
        else:
            key = command[0] + '.' + command[1]
            ob = obj.get(key, None)
            if key in obj:
                attr = command[2]
                attr_value = command[3]
                setattr(ob, attr, attr_value.lstrip('"').rstrip('"'))
                models.storage.save()
            else:
                if command[0] in HBNBCommand().class_names:
                    print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        ''' Prints all string representation of all instances '''
        command = line.split()
        str_list = []
        obj = models.storage.all()
        if len(command) < 1:
            for items in obj.values():
                str_list.append(items.__str__())
            print(str_list)
        elif command[0] in HBNBCommand().class_names:
            full_class_name = eval(command[0] + "()")
            new_instance = full_class_name
            for items in obj.values():
                if items.__class__.__name__ == command[0]:
                    str_list.append(items.__str__())
            print(str_list)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        obj = models.storage.all()
        i = 0
        try:
            splited = line.split(".")
            class_name = splited[0]
            cmd = splited[1].replace("()", "")
            if cmd == "all":
                HBNBCommand().do_all(class_name)
            elif cmd == 'count':
                for items in obj.values():
                    if class_name == items.__class__.__name__:
                        i = i + 1
                if i != 0:
                    print(i)
                else:
                    print("** class doesn't exist **")
            elif cmd.startswith('show'):
                cmd_id = splited[1].split("(")
                id_ = cmd_id[1].replace(")", "")
                id_ = id_.replace("\"", "")
                line = class_name + " " + id_
                HBNBCommand().do_show(line)
            elif cmd.startswith('destroy'):
                cmd_id = splited[1].split("(")
                id_ = cmd_id[1].replace(")", "")
                id_ = id_.replace("\"", "")
                line = class_name + " " + id_
                print(line)
                HBNBCommand().do_destroy(line)
            elif cmd.startswith('update'):
                cmd_id = splited[1].split("(")
                id_ = cmd_id[1].replace(")", "")
                id_ = id_.replace("\"", "")
                line = class_name + " " + id_
                line = line.replace(",", "")
                print(line)
                HBNBCommand().do_update(line)
            else:
                print(f"*** Unknown syntax: {line}")
        except IndexError:
            print(f"*** Unknown syntax: {line}")

    def do_quit(self, line):
        ''' exit the cmd '''
        return True

    def emptyline(self):
        ''' new line if command is empty '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
