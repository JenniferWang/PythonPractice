#-*-coding: UTF-8 -*-
#Numpy data structure
import numpy as np
#import numpy
#from numpy import *

#                     Create Arrays                    
#_________________________________________________________
#Arrays
#尽量不要使用matrix，效率问题
#create from a list
a = np.array([1, 4, 5, 8], float)
type(a)


#other ways to create arrays
#dtype默认可能是float
np.arange(5, dtype = float) #arange is similar to range but returns an array
np.arange(5, dtype = int)

np.zeros(7, dtype = int)
np.ones((2,3), dtype = float)

np.zeros_like(a) #create a new array with the same dimensions and type of an existing one
np.ones_like(a)

#create special 2D matrix
np.identity(4, dtype = float) #create an identity matrix of a given size.
np.eye(4, k=1, dtype = float) #returns matrices with ones along the kth diagonal
#access, slice, manipulate
a[:2] #first 2 elements
a[0] = 5

#multidimensional case
b = np.array([[1,2,3], [4,5,6]], float)
b[1,:] #':' in a dimension indicates the use of everything along that dimension
b[-1:,-2:] #last row and last two colomns

#sort
a = np.array([6, 2, 5, -1, 0], float)
sorted(a)
a.sort()
#Values in an array can be "clipped" to be within a prespecified range. 
a = np.array([6, 2, 5, -1, 0], float)
a.clip(0, 5)
#Extract unique elements
np.unique(a)
#Extract diagonal
a = np.array([[1, 2], [3, 4]], float)
a.diagonal()

#                     Array Properties                    
#_________________________________________________________
#size
a.shape
b.shape

#datatype
a.dtype

#length of first axis
len(a)
len(b)

# test if values are present
2 in b
0 in b

#reshape an array
a = np.array(range(10),float)
a.reshape((5,2))
a.shape

#Python's name-binding approach still applies to arrays. The copy functioncan be used to create a new, separate copy of an array in memory if needed
c = a.copy()

#create lists from arrays:
a.tolist()

#convert the raw data in an array to a binary string
s = a.tostring()
np.fromstring(s)

#fill an array with a single value
#keep the dimension unchanged
a.fill(0)

#transpose
a = np.array(range(6), float).reshape((2, 3))
a.transpose()
a.T
#                     Concatinate                    
#_________________________________________________________
#convert multi-dimensional arrays to one-dimensional arrays
a.flatten()

#concatenate two or more arrays
#合并
a = np.array([1,2], float)
b = np.array([3,4,5,6], float)
c = np.array([7,8,9], float)
np.concatenate((a,b,c)) # combine a,b,c in a tuple
#by default, NumPy concatenates along the first dimension
a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7,8]], float)
np.concatenate((a,b))
np.concatenate((a,b), axis=0)
np.concatenate((a,b), axis=1)

#increase the dimension of an array
a = np.array([1, 2, 3], float)
a[:,np.newaxis]
#                     Item selection                     
#_________________________________________________________
#Array item selection and manipulation
#use array selectors to filter for specific subsets of elements of other arrays.
a = np.array([[6, 4], [5, 9]], float)
a >= 6
a[a >= 6]
a[np.logical_and(a > 5, a < 9)]
#select using integer arrays
a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)
a[b]
a.take(b) #equivalent to a[b]
# there is a 'put' function
a[[0, 0, 1, 3, 2, 1]] # Lists can also be used as selection arrays
a = np.array([[1, 4], [9, 16]], float) #multidimensional
b = np.array([0, 0, 1, 1, 0], int)
c = np.array([0, 1, 1, 1, 1], int)
a[b,c]
a.take(b, axis=0)
a.take(b, axis=1)

#                     Array mathematics                    
#_________________________________________________________
#Basic array operations
a = np.array([2, 4, 3], float)
a.sum()
np.sum(a)
a.prod()
np.prod(a)
#Array mathematics
a = np.array([1,2,3], float)
b = np.array([5,2,6], float)
a + b
a – b
a * b # elementwise multiplication
b / a # elementwise division
a % b # elementwise remainder
b**a  # elementwise power

#If arrays do not match in size
a = np.array([1,2,3], float)
b = np.array([4,5], float)
#Error

#If arrays do not match in dimensions
#They will be broadcasted by Python to perform the operation
#This often means that the smaller array will be repeated as necessary to perform the operation indicated. 
a = np.array([[1, 2], [3, 4], [5, 6]], float)
b = np.array([-1, 3], float)
a + b

#Use the 'newaxis' constant to specify how we want to broadcast:
a = np.zeros((2,2), float)
b = np.array([-1., 3.], float)
a + b[np.newaxis,:]
a + b[:,np.newaxis]

#arrays that do not match in the number of dimensions will be broadcasted by Python 

#矩阵 运算 计算
#Vector and matrix mathematics
a = np.array([[0, 1], [2, 3]], float)
b = np.array([2, 3], float)
c = np.array([[1, 1], [4, 0]], float)
np.dot(b, a)
np.dot(a, b)
np.dot(a, c)

a = np.array([1, 4, 0], float)
b = np.array([2, 2, 1], float)
np.outer(a, b)
np.inner(a, b)
#array.shape属性的问题，就算写成a.T.dot(b)和a.dot(b)效果是一样的
#解决方案，指定shape
#instead of using 'a = np.array([1, 4, 0], float)'
#use:
a = np.array([1, 4, 0], float).reshape(1,3)
b = np.array([2, 2, 1], float).reshape(1,3)
a.T.dot(b)

#Numpy matrix
a = np.matrix("4 3 5; 6 7 8; 1 3 13; 7 21 9")
b = np.matrix("7 8 15; 5 3 11; 7 4 9; 6 15 4")
a.T * b #matrix multiplication

#                     linalg submodule                   
#_________________________________________________________
a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
np.linalg.det(a) #determinant
vals, vecs = np.linalg.eig(a)
b = np.linalg.inv(a)# inverse
U, s, Vh = np.linalg.svd(a) # SVD

#to perform mathematical operations. This often means that the smaller array will be repeated as necessary to perform the operation indicated. 
#common mathematical functions:
#they are applied elementwise to arrays
#abs, sign, sqrt, log, log10, exp, sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, arcsinh, arccosh,andarctanh.
#floor, ceil, and rint give the lower, upper, or nearest (rounded) integer

#important constants:
np.pi
np.e

#                     Array iteration                    
#_________________________________________________________

#Array iteration
#one-dimensional array
a = np.array([1, 4, 5], int)
for x in a:
	print(x) #similar to that of lists
#multi-dimensional array
#iteration proceeds over the first axis
a = np.array([[1, 2], [3, 4], [5, 6]], float)
for x in a:
	print(x) 
#multiple assignment
a = np.array([[1, 2], [3, 4], [5, 6]], float)
for (x,y) in a:
	print(x,y)

#                     Array Statistics                    
#_________________________________________________________
#statistical quantities: mean, variance, standard deviation
a.mean()
a.var()
a.std()
np.median(a)
#correlation coefficient for multiple variables
a = np.array([[1, 2, 1, 3], [5, 3, 1, 8]], float)
c = np.corrcoef(a)
#covariance
np.cov(a)

#min and max
a.min()
a.max()
#argmin,argmax: return the array indices of the minimum and maximum values:
a.argmin()
a.argmax()
#For multidimensional arrays, use 'axis'
a = np.array([[0, 2], [3, -1], [3, 5]], float)
a.mean(axis=0)
a.mean(axis=1)




#             Comparison operators and value filtering                   
#_________________________________________________________
#Return boolean values
a = np.array([1, 3, 0], float)
b = np.array([0, 3, 2], float)
c = a > b
a == b
a <= b
a > 2 #Arrays can be compared to single values using broadcasting

#determine whether or not any or all elements of a Boolean array are true
c = np.array([ True, False, False], bool)
any(c)
all(c)

#Compound Boolean expressions
#(Elementwise) logical_and, logical_or, and logical_not.
a = np.array([1, 3, 0], float)
np.logical_and(a > 0, a < 3)
b = np.array([True, False, True], bool)
np.logical_not(b)
c = np.array([False, True, False], bool)
np.logical_or(b, c)

#'where' function, implement a Boolean filter
#where(boolarray, truearray, falsearray)
a = np.array([1, 3, 0], float)
b = np.where(a != 0, 1 / a, a)
#i.e. if boolarray[i]==True: b[i] = truearray[i]; else: b[i] = falsearray[i]
np.where(a > 0, 3, 2) #Broadcasting can also be used with the where function

#Functions that tests the values in an array
a = np.array([[0, 1], [3, 0]], float)
a.nonzero() #returns tuple of indices of the nonzero values 
a = np.array([1, np.NaN, np.Inf], float) #infinity and NAN
np.isnan(a)
np.isfinite(a)


#             Randomize/ Random Numbers                    
#_________________________________________________________
#Random numbers:
#set a seed for debugging purpose
np.random.seed(293423)
#generate two-dimensional random arrays
#range: [0.0, 1.0) 
np.random.rand(2,3)
np.random.rand(6).reshape((2,3))
#generate random integers
#[min, max) 
np.random.randint(5, 10)
#Other distributions
np.random.poisson(6.0)
np.random.normal(1.5, 4.0)
np.random.normal() #𝜇 = 0, 𝜎 = 1
#draw multiple values
np.random.normal(size=5)

#shuffle the order
l = range(10)
np.random.shuffle(l)




