# Create a class “Programmer” for storing information of few programmers working at Microsoft

class Programmer:
    def __init__ (self,name,role,experience,salary):
        self.name = name
        self.role = role
        self.experience = experience
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Role: {self.role}, Experience: {self.experience} years, Salary: ${self.salary}")


#Write a class Calculator capable of finding square, cube and square root of a number

import math
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)
    
"""
Create a class with a class attribute a; create an object from it and set (a)
directly using object.a = 0. Does this change the class attribute?
"""
class MyClass:
    a = 10  # class attribute  
object = MyClass()
print("Before changing, class attribute a:", MyClass.a)  # Output: 10
object.a = 0  # setting a directly using object
print("After changing, class attribute a:", MyClass.a)  # Output: 10
print("Object attribute a:", object.a)  # Output: 0
# No, changing object.a does not change the class attribute MyClass.a
#The object now has its own attribute 'a' that shadows the class attribute

"""
Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. 
"""
class TestClass:
    def __init__(me, value):
        me.value = value  # using 'me' instead of 'self'

    def display(me):
        print(f"Value: {me.value}")

test_object = TestClass(42)
test_object.display()  # Output: Value: 42
# Yes, you can change the self-parameter to something else like 'me' or 'slf'