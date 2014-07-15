#decorator practice
#http://www.cnblogs.com/Jerry-Chou/archive/2012/05/23/python-decorator-explain.html
#version 1
def login():
	print('in login')

def printdebug(func):
	"""
	con:每次调用func都要通过printdebug调用
	"""
	print('enter the login v1')
	func()
	print('exit the login v1')

printdebug(login)


#version2
login2 = login 
def printdebug2(func):
	"""
	返回函数
	"""
	#def __decorator(func):
	def __decorator():
		print('enter the login v3')
		func()
		print('exit the login v3')
	return __decorator

debug_login = printdebug2(login2)
debug_login()

#version3
@printdebug2 # login3= printdebug2(login3)
def login3():
	"""
	不带参数
	"""
	print('in login3')

login3()

#version4 
def printdebug4(func):
	"""
	login带参数形式
	"""
	def __decorator(user):
		print('enter the login v4')
		func(user)
		print('exit the login v4')
	#return __decorator(user)
	return __decorator

@printdebug4
def login4(user):
	print('in login: ' + user)

login('Jennifer')

#version5
def printdebug_level(level): 
	"""
	Recall that parenthesis in Python are the call operator.

	@printdebug_level(level = 5) means call function printdebug_level with parameter level =5, and we get a specific function printdebug5(func) in return, and then use printdebug5(func) as the decorator

	printdebug_level(level) is called wrapper.
	"""
	def printdebug5(func):
		def __decorator(user):
			print('enter the login v5'+str('level'))
			func(user)
			print('exit the login')
		return __decorator
	return printdebug5

@printdebug_level(level = 5) 
def login5(user):
	print('in login: '+user)

login5('Jennifer')








