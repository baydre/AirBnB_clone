#!/usr/bin/python3
''' console 0.0.1 '''
import cmd
from models.base_model import BaseModel
# from models import classes
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from shlex import split
import re

def parse(arg):
    '''
        Ussage:
            Search for text enclosed in curly braces
            using a regular expression
    '''
    curly_braces = re.search(r"\{(.*?)\}", arg)
    
    '''
        Usage:
            Search for text enclosed in square brackets
            using a regular expression
    '''
    brackets = re.search(r"\[(.*?)\]", arg)
    
    '''
        Usage:
            Check if there sre no curly braces found in
            the input string
    '''
    if curly_braces is None:
        
        '''
            Usage:
                Check if there are no square brackets
                found in the input string
        '''
        if brackets is None:
            '''
                If neither curly braces nor square brackets
                are present, split the input string by commas
            '''
            return [i.strip(",") for i in split(arg)]
        else:
            '''
                If square brackets are found,
                split the input string up to the end of the brackets
            '''
            lexer = split(arg[brackets.span()[0]])
            
            '''
                Remove trailing commas and create a list of
                split items
            '''
            my_list = [i.strip(",") for i in lexer]
            
            '''
                Append the contents of
                the square brackets to the list
            '''
            my_list.append(brackets.group())
            
            '''
                Return the final list
            '''
            return my_list
        # end else
    else:
        '''
            If there are curly brces in the input string
            Split the input string up to the end of the curly braces
        '''
        lexer = split(arg[:curly_braces.span()[0]])
        
        '''
            Remove trailing commas and
            create a list of split items
        '''
        my_list = [i.strip(",") for i in lexer]
        
        '''
            Append the contents of the curly braces to the list
        '''
        my_list.append(curly_braces.group())
        
        '''
            Return the final list
        '''
        return my_list
    # end else


class HBNBCommand(cmd.Cmd):
    '''
        cmdln - interpreter class
    '''
    prompt = '(hbnb) '
    __classes = {
            'BaseModel',
            'User',
            'State',
            'City',
            'Place',
            'Amenity',
            'Review'
    }

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
        args = parse(line)
        if not args or len(args) == 0:
            '''If class is missing '''
            print('** class name missing **')
            return
        # end if
        elif args[0] not in self.__classes:
            ''' if it doe not exist '''
            print("** class doesn't exist **")
            return
        # end elif
        else:
            print(eval(args[0])().id)
            storage.save()
            return
        # end else

    def do_show(self, line):
        '''shows an instance'''
        args = parse(line)
        if not args or len(args) == 0 or args[0] == "":
            '''
                if class is missing
            '''
            print('** class name missing **')
        elif args[0] not in self.__classes:
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
        args = parse(line)
        cl_nm = '{}.{}.format(args[0], args[1])'
        objects = storage.all()

        if len(args) == 0:
            ''' If class is missing '''
            print('** class name missing **')
            return False
        # end if
        # elif cl_nm not in classes:
        elif args[0] not in self.__classes:
            '''
                if class does not exist
            '''
            print("** class doesn't exist **")
            return False
        # end elif
        elif len(args) == 1:
            '''
                If the id is missing
            '''
            print('** instance id missing **')
            return False
        # end elif
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
        args = parse(line)
        objects = storage.all()
        if len(args) > 0:
            if args[0] not in self.__classes:
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
            Usage:
                updates instance
        '''
        args = parse(line)
        objects = storage.all()

        if len(args) < 2:
            '''
                checking the lenght of args:
                    At least 2 elements are needed:
                    - The class name (args[0])
                    - The instance id (args[1])
            '''
            print('** class name missing **')
            return False
        # end if

        class_name = args[0]
        # key = '{}.{}'.format(class_name, args[1])
        key = args[0] + '.' + args[1]

        if class_name not in self.__classes:
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
            data_type = {str, float, int}
            for i, val in eval(args[2]).items():
                if i in my_dict.key() and type(my_dict[i]) in data_type:
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
