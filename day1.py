import pyttsx3
import os

engine = pyttsx3.init()
engine.say("hiiiii guys")
engine.runAndWait()

print("Hello World")

#for single line comment instead of // in cpp

""" or ''' can be used as well
for multi line comment instead of /* */ in cpp
"""
print("This is Day 1 of Python Programming")

# Python is an interpreted language, so no need to compile like in C++ or Java

#installed python text to speech


def print_directory_contents(path):
    try:
        # os.listdir() returns a list of all files and directories in the specified path
        contents = os.listdir(path)
        
        print(f"Contents of '{path}':")
        print("-" * 20)
        
        for item in contents:
            print(item)
            
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")

# Example usage:
# '.' represents the current directory
current_directory = "." 
print_directory_contents(current_directory)