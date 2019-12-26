def enter_age():
	age =input("enter your good age: ")
	return int(age)
	
def insecond():
	age = enter_age()
	second = age * 60 * 60 * 365 * 24
	print("your lived: ",second, "second")
insecond()