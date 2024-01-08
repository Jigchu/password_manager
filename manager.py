from fernet import fernet
from data import retrive_data
import qna

def manager():
	pass

def lookup():
	passwords = retrive_data()
	if passwords == None:
		print("No passwords to lookup")
		return
	apps = [app for app in passwords]
	app = qna.mcq("Which app's password would you like to view?", apps)

def update():
	pass