#!/usr/bin/python3
import cmd
import models
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
	intro = ''
	prompt = '(hbnb) '
	classes = ["BaseModel"]


	# ----- Basic HBNB commands -----
	def do_create(self, arg):
		""" Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel """
		if arg == "":
			print("** class name missing **")
		elif arg not in self.classes:
			print("** class doesn't exist **")
		else:
			n = BaseModel()
			n.save()
			print(n.id)

	def do_show(self, arg):
		""" Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234 """
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
				print ("** no instance found **")
			else:
				print(models.storage.all()[s])

	def do_destroy(self, arg):
		"""  Deletes an instance based on the class name and id (save the change into the JSON file). """
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
				print ("** no instance found **")
			else:
				del models.storage.all()[s]
				models.storage.save()

	def do_all(self, arg):
		""" Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all. """
		r = []
		if arg:
			if arg not in self.classes:
				print("** class doesn't exist **")
				return
			else:
				for key, value in models.storage.all().items():
					if arg in key:
						r.append(value.__str__())
		else:
			for key, value in models.storage.all().items():
				r.append(value.__str__())
		print(r)

	def do_update(self, arg):
		""" Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com". """
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
				print ("** no instance found **")
			elif len(a) == 2:
				print("** attribute name missing **")
			elif len(a) == 3:
				print("** value missing **")
			else:
				ob = models.storage.all()[s]
				setattr(ob, a[2],  a[3])
				ob.save





	# ------

	def do_quit(self, arg):
		""" Quit command to exit the program """
		return True

	def do_EOF(self, arg):
		""" Quit command to exit the program """
		return True

def parse(arg):
    """ Convert a series of zero or more space separated strings to a list """
    return shlex.split(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
