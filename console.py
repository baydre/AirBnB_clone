#!/usr/bin/python3
'''
    The HBNB console
'''
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


def parse(line):
    '''
        Ussage:
            Search for text enclosed in curly braces
            using a regular expression
    '''
    curly_braces = re.search(r'\{(.*?)\}', line)
    '''
        Usage:
            Search for text enclosed in square brackets
            using a regular expression
    '''
    brackets = re.search(r'\[(.*?)\]', line)
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
            return [arg.strip(',') for arg in split(line)]
        # end if
        else:
            '''
                If square brackets are found,
                split the input string up to the end of the brackets
            '''
            lexer = split(line[:brackets.span()[0]])
            '''
                Remove trailing commas and create a list of
                split items
            '''
            my_list = [arg.strip(',') for arg in lexer]
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
    # end if
    else:
        '''
            If there are curly brces in the input string
            Split the input string up to the end of the curly braces
        '''
        lexer = split(line[:curly_braces.span()[0]])
        '''
            Remove trailing commas and
            create a list of split items
        '''
        my_list = [arg.strip(',') for arg in lexer]
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
            Usage:
                `Empty line + ENTER` do nothing
        '''
        pass
    # end method

    def do_quit(self, line):
        '''
            Usage:
                Quit command to exit the program
        '''
        return True
    # end method

    def do_EOF(self, line):
        '''
            EOF command to exit program
        '''
        print('')
        return True
    # end method

    def do_create(self, line):
        '''
            creates a new instance of class BaseModel,
                saves it to JSON file and print the id
        '''
        args = parse(line)
        if not args or len(args) == 0:
            '''If class is missing '''
            print('** class name missing **')
        # end if
        elif args[0] not in self.__classes:
            ''' if it doe not exist '''
            print("** class doesn't exist **")
        # end elif
        else:
            print(eval(args[0])().id)
            storage.save()
        # end else
    # end method

    def do_show(self, line):
        '''shows an instance'''
        args = parse(line)
        objects = storage.all()
        if not args or len(args) == 0 or args[0] == "":
            '''
                if class is missing
            '''
            print('** class name missing **')
        # end if
        elif args[0] not in self.__classes:
            '''
                if class does not exist
            '''
            print("** class doesn't exist **")
        # end elif
        elif len(args) < 2 or args[1] == '':
            '''
                command without an argument
            '''
            print('** instance id missing **')
        # end elif
        else:
            key = '{}.{}'.format(args[0], args[1])
            if key in objects:
                print(objects[key])
            # end if
            else:
                print('** no instance found **')
            # end else
        # end else
    # end method

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
        elif args[0] not in HBNBCommand.__classes:
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
            # end if
            else:
                '''
                    If the instance of the class name
                    doesn’t exist for the id
                '''
                print('** no instance found **')
            # end else
        # end method

    def do_all(self, line):
        '''
        Usage:  all | all <class>
            prints all instance
        '''
        args = parse(line)
        objects = storage.all()
        if len(args) > 0 and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return False
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
                # end if
                elif len(args) == 0:
                    objects.append(obj.__str__())
                # end elif
            # end for
            print(objects)
        # end else
    # end method

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

        if class_name not in HBNBCommand.__classes:
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

    def default(self, line):
        '''
            Usage:
                Behaviour when module input is invalid
        '''
        '''
            Create a dictionary that maps commands
            to their corresponding methods.
        '''
        my_default_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }
        '''
            Check to see if the input argument contains a period
            (this indicates a method call).
        '''
        match = re.search(r'\.', line)

        if match is not None:
            '''
                Usage:
                    Split the argument into two parts
                    before and after the period
            '''
            args = [line[:match.span()[0]], line[match.span()[1]:]]

            '''
                search for text enclosed in parentheseees
            '''
            match = re.search(r'\((.*?)\)', args[1])

            if match is not None:
                '''
                    Split the method call into the command and parameters
                '''
                my_command = [args[1][:match.span()[0]], match.group()[1:-1]]

                if my_command[0] in my_default_dict.keys():
                    '''
                        if the command is valid,
                        construct the full command and call the method
                    '''
                    key = '{}.{}'.format(args[0],my_command[1])
                    key_const = my_default_dict[my_command[0]](key)
        '''
            If the input does not match any of the syntax(knownn),
                print the error message
        '''
        # print('*** Unknown syntax: {}'.format(line))
        return False
    def do_count(self, line):
        '''
            Usage:
                This used to retrieve
                the number of instances of a class:
                    <class name>.count()
        '''
        # Parse the input argument to identify the class name
        args = parse(line)
        if not args:
            return False

        # the counter
        counter = 0
        '''
            We Iterate through all instances stored in the 'storage'
        '''
        for inst in storage.all().values():
            '''
                we checck if class name of instance
                matches the provided class name
            '''
            if args[0] == inst.__class__.__name__:
                ''' increment count '''
                counter += 1
            # end if
        # end for
        print(counter)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
