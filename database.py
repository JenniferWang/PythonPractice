#database.py 
#use python 3.4 
import sys, shelve
def store_person(db):
	"""
	Query user for data and store it in the shelf object
	"""
	pid = input('Enter unique ID number: ')
	person = {}
	person['name'] = input('Enter name: ')
	person['age'] = input('Enter age: ')
	person['phone'] = input('Enter phone number: ')

	db[pid] = person

def lookup_person(db):
	"""
	Query user for ID and desired field, and fetch the corresponding data from the shelf object
	"""

	pid = input('Enter ID number: ')
	field = input('What would you like to konw? (name, age, phone) ')
	field = field.strip().lower()
	print(field.capitalize() +':' ??
        Now I am making some change on my Mac
