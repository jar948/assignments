def multiply(a,b):
		return a * b

def add(a,b):
		return a + b

def subtract(a,b):
		return a - b

def divide(a,b):
		return a / b
		
def square(a):
		return a ** 2

def cube(a):
		return a ** 3

def square_n_times(a,b):
		return a ** b

print "I'm going to use the calculator functions to multiply 5 and 6"
x = multiply(5,6)
print x

print "I'm going to use the calculator functions to square 5"
x = square(5)
print x

print "I'm going to use the calculator functions to cube 5"
x = cube(5)
print x

print "I'm going to use the calculator functions to square 5 five times"
x = square_n_times(5,5)
print x
