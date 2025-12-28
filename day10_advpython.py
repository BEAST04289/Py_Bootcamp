# from typing import Annotated
from os import name
from typing import List, Tuple, Dict, Union, Optional
# List - used to define a list of elements of a specific type.
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple - used to define a fixed-size collection of elements of specific types.
point: Tuple[str, int] = ("x-mas", 20)
# Dict - used to define a dictionary with specific key and value types.
person: Dict[str, Union[str, int]] = {"name": "Alice", "age": 30}
# Union - used to indicate that a variable can be of multiple types.
data: Union[int, str] = "Hello"
# Optional - used to indicate that a variable can be of a specific type or None.
optional_data: Optional[int] = None

#walrus operator is used to assign values to variables as part of a larger expression.
# It is represented by the symbol := and is also known as the assignment expression.
# it allows you to assign a value to a variable while simultaneously using that value in an expression.
if (n := len([1, 2, 3, 4, 5])) > 3: 
 print(f"List is too long ({n} elements, expected <= 3)") 
# Output: List is too long (5 elements, expected <= 3)

#type definition - helpful in annotating variables, function parameters, and return types.
# It enhances code readability and helps with static type checking.

n : int = 10
pi : float = 3.14
def greet(name: str) -> str:
    return f"Hello, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!

def add(a: int, b: int) -> int: 
    return a + b

# match statement - used for pattern matching, similar to switch-case statements in other languages.
def http_status(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
print(http_status(200))  # Output: OK

#exception handling helps manage errors gracefully without crashing the program.

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else: # executes if no exceptions occur and the try block is successful
    print("Division performed successfully.")
    #even if the function returns from the try or except block, the finally block will still execute
finally: # executes regardless of whether an exception occurred or not
    print("Execution completed.")

    def myFun():
        print("Hello")
    
myFun()
print(__name__) # Output: __main__  but if imported, it will print the module name
#import format - from module import myFun
#myFun()
if name == "__main__":
    print("This code is running directly and not imported.")
  
from day9_inheritence import Staff, Worker  
@Worker.salary.getter
def salary(self):
    return self._salary

#global and nonlocal keywords
def outer_function():
    outer_var = "I am outside!"
    inner_var = "I am inside!"

    def inner_function():
        global outer_var
        nonlocal inner_var
        outer_var = "I have been modified!"
        inner_var = "I have also been modified!"
        print(inner_var)
        print(outer_var)

    inner_function()
    print(outer_var)
outer_function()

#enumrate function - adds a counter to an iterable and returns it as an enumerate object.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#list comprehension - provides a concise way to create lists.
myList= [x for x in range(10)]
print(myList)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sq=[x**2 for x in myList]
print(sq)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]


#virtual environments - isolated Python environments that allow you to manage dependencies for different projects separately.
# To create a virtual environment, use the command: python -m venv myenv
# To activate the virtual environment:
# On Windows: myenv\Scripts\activate

#pip freeze - lists all installed packages in the current environment along with their versions.
# To save the list to a requirements.txt file, use the command: pip freeze > requirements.txt
# To install packages from a requirements.txt file, use the command: pip install -r requirements.txt
 
