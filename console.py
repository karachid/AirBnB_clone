#!/usr/bin/python3
'''Define class HBNBCommand'''
import cmd
from models import BaseModel, storage


class HBNBCommand(cmd.Cmd):
    '''class HBNBCommand'''

    prompt = "(hbnb) "

    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id'''
        if len(line.split()) != 1:
            return
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            b = BaseModel()
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
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
            elif args[1] and len(args) == 2:
                dic = self.make_dict()
                if args[1] not in dic:
                    print("** no instance found **")
                else:
                    print(dic[args[1]])

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
            elif args[1] and len(args) == 2:
                dic = self.make_dict()
                if args[1] not in dic:
                    print("** no instance found **")
                else:
                    dic = storage.all()
                    del dic["BaseModel." + args[1]]
                    storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances based or not
        on the class name'''
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
        elif not arg or arg == "BaseModel":
            dic = self.make_dict()
            list_obj = []
            for obj in dic.values():
                list_obj.append(str(obj))
            print(list_obj)

    def do_update(self, line):
        '''Updates an instance based on the class name and id by adding or
        updating attribute'''
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
            elif args[1] and len(args) >= 2:
                dic = self.make_dict()
                if args[1] not in dic:
                    print("** no instance found **")
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(args) == 3:
                            print("** value missing **")
                        else:
                            obj = dic[args[1]]
                            if args[3][0] == '"':
                                values = args[3].split('"')
                                value = values[1]
                            else:
                                value = args[3]
                            setattr(obj, args[2], value)
                            print(obj)
                            storage.save()

    def emptyline(self):
        pass

    def do_EOF(self, line):
        '''EOF command to exit the program\n'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
