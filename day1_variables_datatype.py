a=234
b=234.56
name_me="SHAURYAAAAA"
c=float(a) #type casting from int to float
d=int(b)   #type casting from float to int
print(a+b) 
print("The name is ",name_me) #string concatenation
print(f"The name is {name_me} and the value of a is {a}") #f-string
print(type(a)) #printing datatype of variable  
print(type(c))
print(type(d))
e=input("Enter your name: ") #taking input from user
print(f"Hello {e}, welcome to Python programming!")
a=input("Enter first number: ")
b=input("Enter second number: ")
print("The sum is: ", int(a)+int(b)) #type casting input strings to int and adding otherwise it wil print a and b together and not their sum