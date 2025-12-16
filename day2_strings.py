name="SHAURYA" #string can be declared using "" or ''
#for multi line string we can use ''' ''' or """ """
name2=name[0:2] #string slicing (excludes 3rd index)
print(name2) #prints first two characters
print(name[2:]) #prints string from index 2 to end
print(name[:4]) #prints string from start to index 3
print(name[1]) #prints character at index 1
print(name[-1]) #prints last character
print(name[-4:]) #prints last 4 characters
print(name[::2]) #prints string with a step of 2
print(name[1:6:3]) #prints string from index 1 to 5 with a step of 3
print(name[::-1]) #prints string in reverse order
print(len(name)) #prints length of string
print(name.lower()) #prints string in lowercase
print(name.upper()) #prints string in uppercase
print(name.replace("A","@")) #replaces all occurrences of A with @  
print(name.split("U")) #splits string at U and returns a list
print(name.find("R")) #returns index of first occurrence of R
print(name.count("A")) #returns count of A in string
print(name.startswith("S")) #returns True if string starts with S
#startswith and endswith are case sensitive
print(name.endswith("A")) #returns True if string ends with A
print(name.capitalize()) #capitalizes first character of string not other characters
print(name.title()) #capitalizes first character of each word in string
print(name.isalpha()) #returns True if all characters in string are alphabets
print(name.isdigit()) #returns True if all characters in string are digits
print(name.isalnum()) #returns True if all characters in string are alphanumeric

#escape sequences in strings
print("Hello\nWorld") #prints Hello and World in new line
print("Hello\tWorld") #prints Hello and World with a tab space
print("He said \"Hello World\"") #prints He said "Hello World"
print('It\'s a beautiful day') #prints It's a beautiful day
print("C:\\Users\\Shaurya") #prints C:\Users\Shaurya
