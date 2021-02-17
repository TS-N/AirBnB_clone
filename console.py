#!/usr/bin/python3
""" This is the console for HBnB project
that allow interaction with database from terminal """
import cmd
import re
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBnB Console
        Allow to interact with the data storage in an easy way
        Works in interactive and non-interactive mode
    """
    intro = ''
    prompt = '(hbnb) '
    classes = [
                "BaseModel",
                "User",
                "City",
                "State",
                "Amenity",
                "Place",
                "Review"
                ]

    def onecmd(self, s):
        x = re.compile('^[A-Z][A-Za-z]+\.[a-z]+\(.*\)$')
        if x.match(s):
            l = sp_parse(s)
            newstr = l[0][1] + ' ' + l[0][0]
            for i in range(0, len(l[1])):
                newstr += ' ' + l[1][i]
            return cmd.Cmd.onecmd(self, newstr)
        else:
            return cmd.Cmd.onecmd(self, s)

    # ----- Basic HBNB commands -----
    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
                and prints the id.
            Ex: $ create BaseModel
        """
        a = parse(arg)
        if a == []:
            print("** class name missing **")
        elif a[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            n = eval(a[0] + "()")
            n.save()
            print(n.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance
                based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
        """
        a = parse(arg)
        if a == []:
            print("** class name missing **")
        elif a[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        else:
            s = "{}.{}".format(a[0], a[1])
            if s not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[s])

    def do_destroy(self, arg):
        """  Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        a = parse(arg)
        if a == []:
            print("** class name missing **")
        elif a[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        else:
            s = "{}.{}".format(a[0], a[1])
            if s not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[s]
                models.storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
                based or not on the class name.
            Ex: $ all BaseModel or $ all.
        """
        r = []
        a = parse(arg)
        if a != []:
            if a[0] not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                for key, value in models.storage.all().items():
                    if a[0] in key:
                        r.append(value.__str__())
        else:
            for key, value in models.storage.all().items():
                r.append(value.__str__())
        print(r)

    def do_update(self, arg):
        """ Updates an instance based on the class name
                and id by adding or updating attribute
                (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        a = parse(arg)
        if a == []:
            print("** class name missing **")
        elif a[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        else:
            s = "{}.{}".format(a[0], a[1])
            if s not in models.storage.all():
                print("** no instance found **")
            elif len(a) == 2:
                print("** attribute name missing **")
            elif len(a) == 3:
                print("** value missing **")
            else:
                ob = models.storage.all()[s]
                setattr(ob, a[2],  a[3])
                ob.save

    def do_count(self, arg):
        """ Count the number of instance of a class
        Eg: $ count User
        """
        a = parse(arg)
        if a == []:
            print("** class name missing **")
        elif a[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            cnt = 0
            for key in models.storage.all():
                if a[0] in key:
                    cnt += 1
            print(cnt)

    # ------

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Do nothing if empty line is passed """
        pass


def parse(arg):
    """ Convert a series of zero or more space separated strings to a list """
    return shlex.split(arg)


def sp_parse(arg):
    """ Convert a string of format User.all() to all User """
    a = arg.split('(')
    a[0] = a[0].split('.')
    a[1] = a[1][:-1]
    a[1] = a[1].split(',')
    return a

if __name__ == '__main__':
    HBNBCommand().cmdloop()
