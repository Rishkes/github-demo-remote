#Add implementation
def add(x,y):
	return x+y
#subtract implementation
def subtract(x,y):
	return x-y       #on master branch
#multiply implementation
def multiply(x,y):
	return x*y      #on Bug456 branch


#divide implementation         #on master branch
def divide(x,y):
	if y==0:
		return DIVIDE_BY_0_ERROR
	else:
		return x/y

