#functions 
def greet(name):
    """This function greets the person passed in as a parameter"""
    print(f"Hello, {name}! Welcome aboard.")
def add(a, b):
    """This function returns the sum of two numbers"""
    return a + b 
def factorial(n):   
    """This function returns the factorial of a number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

greet("Alice")
result = add(5, 7)
print(f"The sum of 5 and 7 is: {result}")
fact = factorial(5)
print(f"The factorial of 5 is: {fact}")
# Output:
# Hello, Alice! Welcome aboard.
# The sum of 5 and 7 is: 12
# The factorial of 5 is: 120

def good_morning(name="Guest"): #by default name is Guest
    """This function greets the person with a good morning message"""
    print(f"Good morning, {name}! Have a great day ahead.")
good_morning("Bob")
good_morning()
# Output:
# Good morning, Bob! Have a great day ahead.
# Good morning, Guest! Have a great day ahead.