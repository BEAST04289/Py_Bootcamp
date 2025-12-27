# inheritence means acquiring properties of one class into another class
#parent class - base class - super class
#child class - derived class - sub class

from hmac import new
from os import name
from re import S


class Employee:
   company = "TechCorp"
   def __init__(self, name, position):
       self.name = name
       self.position = position

   def show_details(self):
       print(f"My name is {self.name} and I work as a {self.position} in {self.company}.")
"""
class Developer:
    def show_details(self):
         print(f"My name is {self.name} and I am a {self.position} at {self.company}.")

    def code(self):
        print(f"{self.name} is writing code in {self.language}.")        
"""
class Developer(Employee):  #inheriting from Employee class and adding new properties 
   company = "DevSolutions"
   def __init__(self, name, position, language):
       super().__init__(name, position)
       self.language = language

   def code(self):
         print(f"{self.name} is writing code in {self.language}.")

#types of inheritence
#single inheritence - one child class inherits from one parent class
dev1 = Developer("Alice", "Developer", "Python")
dev1.show_details()
dev1.code()
#multi-level inheritence - one child class inherits from another child class
class SeniorDeveloper(Developer):
   def lead(self):
       print(f"{self.name} is leading the development team.")
senior_dev = SeniorDeveloper("Bob", "Senior Developer", "Java")
senior_dev.show_details()
senior_dev.code()
senior_dev.lead()
#multiple inheritence - one child class inherits from multiple parent classes
class Manager:
   name=""
   def manage(self):
       print(f"{self.name} is managing the team.")
class TeamLead(Developer, Manager,Employee):  #inheriting from both Developer and Manager classes
   def lead_team(self):
       print(f"{self.name} is leading the team.")
team_lead = TeamLead("Charlie", "Team Lead", "C++")
team_lead.show_details()
team_lead.code()
team_lead.manage()
team_lead.lead_team()
#hierarchical inheritence - multiple child classes inherit from one parent class
class Designer(Employee):
   def design(self):
       print(f"{self.name} is designing a new interface.")
designer = Designer("Diana", "Designer")
designer.show_details()
designer.design()
#hybrid inheritence - combination of two or more types of inheritence
class Director(Manager, Employee):
    def direct(self):
         print(f"{self.name} is directing the company's strategy.")
director = Director("Eve", "Director")
director.show_details()
director.manage()
director.direct()
#method resolution order (MRO) - order in which Python looks for a method in a hierarchy of classes
print(TeamLead.mro())  #shows the method resolution order for TeamLead class
print(Director.mro())  #shows the method resolution order for Director class
#use of super() function to call parent class methods and constructors
class Intern(Employee):
   def __init__(self, name, position, duration):
       super().__init__(name, position)
       self.duration = duration

   def show_internship_details(self):
       print(f"{self.name} is an intern for {self.duration} months.")
intern = Intern("Frank", "Intern", 6)
intern.show_details()
intern.show_internship_details()
#overriding methods in child class
class Consultant(Employee):
   def show_details(self):
       print(f"Consultant Name: {self.name}, Position: {self.position}, Company: {self.company}")
consultant = Consultant("Grace", "Consultant")
consultant.show_details()
#adding new methods in child class
class Analyst(Employee):
   def analyze(self):
       print(f"{self.name} is analyzing data.")
analyst = Analyst("Hank", "Analyst")
analyst.show_details()
analyst.analyze()
#accessing parent class methods from child class
class Tester(Employee):
   def test(self):
       print(f"{self.name} is testing the application.")
tester = Tester("Ivy", "Tester")
tester.show_details()
tester.test()

#class methods and static methods in inheritence
#class method - method that is bound to the class and not the instance of the class
#static method - method that does not receive an implicit first argument (neither self nor cls parameter)
class Staff:
    company = "GlobalTech"
    def __init__(self, name, role):
        self.name = name
        self.role = role
    #class method shows only class level data it wont let you access instance level data
    #use cls parameter instead of self
    #static method neither access class level data nor instance level data
    #doesnt let use self or cls parameter
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def staff_policy():
        print("All staff must adhere to company policies.")
#property decorators in inheritence
class Worker(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self._salary = salary  #private attribute

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive.")

_salary = Worker("Jack", "Worker", 50000)
print(_salary.salary)

class SeniorWorker(Staff,Worker):
    @property
    def name(self):
        # Return all name parts capitalized and separated
            return self._name_parts

    @name.setter
    def name(self, new_name):
            # Split the name and capitalize each part, store as a list
            if new_name:
                self._name_parts = [part.capitalize() for part in new_name.split()]
            else:
                self._name_parts = []

e=SeniorWorker("Karen Bla bla", "Senior Worker")
print(e.name)
#ENCAPSULATION - wrapping data and methods into a single unit (class)
#ABSTRACTION - hiding complex implementation details and showing only essential features of the object

#OPERATOR OVERLOADING - defining custom behavior for operators in user-defined classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)    

    def display(self):
        print(f"Point({self.x}, {self.y})")
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
p3.display()  #Output: Point(6, 8)