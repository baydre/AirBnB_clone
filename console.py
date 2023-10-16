#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
