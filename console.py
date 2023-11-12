#!/usr/bin/python3
'''Define class HBNBCommand'''
import cmd
from models import BaseModel, storage, User
from models import Review, State, City, Amenity, Place


class HBNBCommand(cmd.Cmd):
    '''class HBNBCommand'''

    prompt = "(hbnb) "
    className = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity, "Place": Place,
                 "Review": Review}

    def complete_create(self, text, line, begidx, endidx):
        """Custom tab completion for the 'create' command's argument"""
        return [name for name in self.className if name.startswith(text)]

    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id'''
        if len(line.split()) > 1:
            return
        if not line:
            print("** class name missing **")
        elif line not in self.className:
            print("** class doesn't exist **")
        else:
            b = self.className[line]()
            b.save()
            print(b.id)

    @staticmethod
    def make_dict():
        '''
        Return a dictionary with the key: id and value: object
        '''
        dic = {}
        all_objs = storage.all()
        for obj in all_objs.values():
            dic[obj.to_dict()["id"]] = obj
        return dic

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class
        name and id'''
        args = line.split()
        if not className_errors(args):
            return
        if len(args) == 2:
            dic = self.make_dict()
            if args[1] not in dic:
                print("** no instance found **")
            else:
                print(dic[args[1]])

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        args = line.split()
        if not className_errors(args):
            return
        if len(args) == 2:
            dic = self.make_dict()
            if args[1] not in dic:
                print("** no instance found **")
            else:
                dic = storage.all()
                del dic[args[0] + "." + args[1]]
                storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances based or not
        on the class name'''
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in self.className:
            print("** class doesn't exist **")
        else:
            for _, v in all_objs.items():
                if type(v).__name__ == args[0]:
                    print("{}".format(str(v)))

    def do_update(self, line):
        '''Updates an instance based on the class name and id by adding or
        updating attribute'''
        args = line.split()
        if not className_errors(args):
            return
        dic = self.make_dict()
        if len(args) == 2:
            if args[1] not in dic:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
            return
        if len(args) == 3:
            if len(args) == 3:
                print("** value missing **")
        else:
            obj = dic[args[1]]
            if args[3][0] == '"':
                values = args[3].split('"')
            else:
                return
            setattr(obj, args[2], values[1])
            storage.save()

    def emptyline(self):
        pass

    def do_EOF(self, line):
        '''EOF command to exit the program\n'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True


def className_errors(args):
    '''checks errors to run a validate classname'''
    if len(args) == 0:
        print("** class name missing **")
        return False
    if args[0] not in HBNBCommand.className:
        print("** class doesn't exist **")
        return False
    if len(args) == 1:
        print("** instance id missing **")
        return False
    return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
