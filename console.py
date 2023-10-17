#!/usr/bin/python3
''' console 0.0.1 '''
import cmd
from models.base_model import BaseModel
from models import classes
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
        cmdln - interpreter class
    '''
    prompt = '(hbnb) '

    def emptyline(self):
        '''
            Empty line + ENTER
        '''
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

    def do_create(self, line):
        '''
            creates a new instance of class BaseModel,
                saves it to JSON file and print the id
        '''
        if len(line) == 0:
            '''If class is missing '''
            print('** class name missing **')
        elif line[0] not in classes:
            ''' if it doe not exist '''
            print("** class doesn't exist **")
        else:
            '''
            try:
                obj = eval(line)()
                obj.save()
                print(obj.id)
            except Exception:
                print("** class doesn't exist **")
            '''
            print(eval(line[0])().id)
            storage.save()

    def do_show(self, line):
        '''shows an instance'''
        args = line.split()
        if not args or len(args) == 0 or args[0] == "":
            '''
                if class is missing
            '''
            print('** class name missing **')
        elif args[0] not in classes:
            '''
                if class does not exist
            '''
            print("** class doesn't exist **")
        elif len(args) < 2 or args[1] == '':
            '''
                command without an argument
            '''
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        '''
        Usage:  `destroy <class><id>`
                `<class>.destroy(<id>)`

                Deletes the class instance of a given id.
        '''
        args = line.split()
        cl_nm = '{}.{}.format(args[0], args[1]'
        if len(args) == 0:
            ''' If class is missing '''
            print('** class name missing **')
        elif cl_nm not in classes:
            '''
                if class does not exist
            '''
            print("** class doesn't exist **")
        elif len(args) == 1:
            '''
                If the id is missing
            '''
            print('** instance id missing **')
        else:
            key = cl_nm + '.' + args[1]
            objects = storage.all()
            if key in objects:
                '''
                    if exists
                '''
                del objects[key]
                storage.save()
            else:
                '''
                    If the instance of the class name
                    doesn’t exist for the id
                '''
                print('** no instance found **')

    def do_all(self, line):
        '''
        Usage:  all | all <class>
            prints all instance
        '''
        args = line.split()
        objects = storage.all()
        if len(args) > 0:
            if args[0] not in classes:
                print("** class doesn't exist **")
        else:
            '''
            class_name = args[0]
            print([str(obj) for key, obj in objects.items()
                  if key.startswith(class_name)])
            '''
            objects = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objects.append(obj.__str__())
                elif len(args) == 0:
                    objects.append(obj.__str__())
            print(objects)

    def do_update(self, line):
        '''
            updates instance
        '''
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            '''
                checking the lenght of args
            '''
            print('** class name missing **')
            return False
        # end if

        class_name = args[0]
        key = '{}.{}'.format(class_name, args[1])

        if class_name not in classes:
            '''
                the class does not exist
            '''
            print("** class doesn't exist **")
            return False
        # end if

        if len(args) == 1:
            '''
                command without argument
            '''
            print("** instance id missing **")
            return False
        # end if

        if key not in objects.keys():
            '''
                If the instance of the class name
                doesn’t exist for the id
            '''
            print('** no instance found **')
            return False
        # end if

        if len(args) == 2:
            print('** attribute name missing **')
            return False
        # end if

        if len(args) == 3:
            args_type = type(eval(args[2]))
            if args_type != dict:
                raise NameError(print('** value missing **'))
            # end if
            return False
        # end if

        if len(args) == 4:
            objs = objects[key]
            my_dict = objs.__class__.__dict__

            if args[2] in my_dict.keys():
                value_type = type(my_dict[args[2]])
                objs.__dict__[args[2]] = value_type(args[3])
            # end if
            else:
                objs.__dict__[args[2]] = args[3]
            # end else
        # end if
        elif type(eval(args[2])) == dict:
            objs = objects[key]
            for i, val in eval(args[2]).items():
                if i in my_dict.key() and type(my_dict[i]) in {str, float, int}:
                    value_type = type(my_dict[i])
                    objs.__dict__[i] = value_type(val)
                # end if
                else:
                    objs.__dict__[k] = v
                # end else
            # end for
        # end elif
        storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
