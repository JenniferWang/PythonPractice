# generator/ iterator practice
# When the generator function is called, the interpreter will stop
# at the yield/return and "return" the value. The next time when 
# the generator is called, it will start from the last pause spot 
# and continue interpreting the remaining codes.

# 1. try to convert [[1,2],[3,4],[5,6]] --> [1,2,3,4,5,6]
# 2. try to flatten in an recursive way
# 3. try multiple yield in one function

# try to convert [[1,2],[3,4],[5,6]] --> [1,2,3,4,5,6]
nested = [[1,2],[3,4],[5,6]]
def flatten_v1(nested):
	"""
	v1 -- Return a list
	"""
	L = []
	for ele in nested:
		for subele in ele:
			L.append(subele)

	return L

print(flatten_v1(nested))

def flatten_v2(nested):
	"""
	v2 -- Return a generator
	"""
	for ele in nested:
		for subele in ele:
			yield subele

print(list(flatten_v2(nested)))

def flatten_v3(nested):
	"""
	v3 -- Recursive generator, could deal with arbitrarily-nested list
	
	want to do somthing like this:
	Need to be clear:
		recurse on what?

	if SomeBaseCase(say just a number) :
		yield the number
	else:
		go on and flatten further

	"""
	L = []
	try:
		for ele in nested:
			for subele in flatten_v3(ele):
				yield subele

	except TypeError: #In the base case, for loop cannot iterate on a single number
		yield nested

nested = [[[1],2],3,4,[5,[6,7]],8]
print(list(flatten_v3(nested)))

def TryMultipleGenerator():
	"""
	Though it seemed that I have defined two generators, but they will work one by one
	"""
	print('I should be the first generator')
	for i in range(5):
		yield i+1

	print('I should be the second generator')
	for j in range(10):
		yield j*10

g = TryMultipleGenerator()
g.__next__()
#for x, y in TryMultipleGenerator():
#	print(x,y)

