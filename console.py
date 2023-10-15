#!/usr/bin/python3
''' console 0.0.1 '''
import cmd
from models.base_model import BaseModel
from models import classes, storage


class HBNBCommand(cmd.Cmd):
    ''' cmdln-interpreter class '''
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'EOF command to exit program\n'
        return True

''' console 0.1 '''
    def do_create(self, line):
        'creates an instance'
        if not line:
            print('** class name missing **')
        else:
            try:
                obj = eval(line)()
                obj.save()
                print(obj.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        'shows an instance'
        args = line.split()
        if not args or len(args) == 0 or args[0] == "":
            print('** class name missing **')
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2 or args[1] == "":
            print('** instance id missing **')
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        'deletes an instance'
        args = line.split()
        class_name = args[0]
        if not args:
            print('** class name missing **')
        elif class_name not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = class_name + '.' + args[1]
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        'prints all instance'
        args = line.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            print([str(obj) for key, obj in objects.items()
                            if key.startswith(class_name)])
'''
    def do_update(self, line):
        'updates instance'
        args = line.split()
        objects = storage.all()
        if not args:
            print('** class name missing **')
        elif args[0] not in 
'''
if __name__ == '__main__':
    HBNBCommand().cmdloop()
