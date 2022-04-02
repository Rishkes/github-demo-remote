#Add 
def add(x,y):
	return x+y

def subtract(x,y):
	return x-y       #on master branch
#multiply 
def multiply(x,y):
	return x*y      #on Bug456 branch


#divide         #on master branch
def divide(x,y):
	if y==0:
		return DIVIDE_BY_0_ERROR
	else:
		return x/y

