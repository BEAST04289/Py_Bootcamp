#there are 2 types of programming: functional programming and object oriented programming
#OOP is based on the concept of "objects", which can contain data and code: 
#data in the form of fields (often known as attributes or properties)
#code in the form of procedures (often known as methods)
#reusability and modularity are key principles of OOP
#dry aproach - don't repeat yourself reuse code through classes and objects
#class is a blueprint for creating objects
#object is an instance of a class

#defining a class

class Employee:
    #constructor method to initialize object attributes
    # init is a special method called a constructor that is called when an object is created
    # it is used to initialize the attributes of the object
    #dunder method - double underscore before and after the method name which is called automatically by Python
    company = "TechCorp"  #class attribute shared by all instances
    def __init__(self, name, position, salary,company):
        self.name = name
        self.position = position
        self.salary = salary
        self.company = company

    #method to display employee details
    def display_info(self):# imortant to add self parameter
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")
    #static method to display company info (does not require self parameter)
    #no access to or use of instance or class variables
    @staticmethod
    def company_info():
        print("This is a company that values its employees.")
    #method to give a raise
    def give_raise(self, amount):# imortant to add self parameter
        self.salary += amount
        print(f"{self.name} has been given a raise of {amount}. New salary is {self.salary}")
    def greet(self):# imortant to add self parameter because it is an instance method
        print(f"Hello, my name is {self.name} and I work at {self.company}")
#creating objects (instances) of the Employee class
emp1 = Employee("Alice", "Developer", 70000,"TeccccCorp")
emp2 = Employee("Bob", "Designer", 65000,"CreativeInc")
#using methods of the Employee class
emp1.display_info()
emp2.display_info()
emp1.give_raise(5000)
emp1.display_info()
emp2.give_raise(3000)
emp2.display_info()
emp3 = Employee("Charlie", "Manager", 80000,"TechCorp")
emp3.display_info()
emp3.give_raise(7000)
emp3.display_info()
emp4 = Employee("Diana", "Intern", 30000,"TechCorp")
emp4.display_info()
emp4.give_raise(2000)
emp4.display_info()
#instance attributes take prference over class attributes with the same name
emp1.company = "TechCorp"  #class attribute
print(emp1.company)  #prints instance attribute
print(emp2.company)  #prints class attribute

#self parameter refers to the current instance of the class and is used to access variables that belong to the class
#it must be the first parameter of any function in the class
#it is similar to "this" keyword in other programming languages
#note: you do not need to pass the self parameter when calling the method, Python does it automatically

#you can create multiple instances of a class with different attributes
Employee.display_info(emp1)  #calling method using class name and passing instance
Employee.display_info(emp2)  #calling method using class name and passing instance