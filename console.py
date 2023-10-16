#!/usr/bin/python3
# console 0.0.1
import cmd
from models.base_model import BaseModel
from models import classes, storage


class HBNBCommand(cmd.Cmd):
    ''' cmdln-interpreter class '''
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, line):
        '''
            Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''
            EOF command to exit program
        '''
        return True
    '''
    # console 0.1
    def do_create(self, line):
        ''
            creates an instance
        ''
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
        ''
            shows an instance
        ''
        args = line.split()
        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2 or args[1] == "":
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

        ''if not args:
            print('** class name missing **')
        else:
            class_name = args[0]
            objects = storage.all()
            if class_name not in storage.all():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = class_name + '.' + args[1]
                print(objects.get(key, '** no instance found **'))
'''


if __name__ == '__main__':
    HBNBCommand().cmdloop()
