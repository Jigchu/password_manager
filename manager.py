from fernet import fernet
from data import retrive_data
import qna

def manager():
	pass

def lookup():
	passwords = retrive_data()
	apps = [app for app in passwords]
	app = qna.mcq("")
	pass

def update():
	pass