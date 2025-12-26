# file input/output is a way to read from and write to files on your computer.
# This is useful for storing data, configurations, or any information that needs to persist
# beyond the runtime of a program.

f=open("text.txt")  #opens file in read mode by default
content=f.read()    #reads the content of the file
print(content)      #prints the content of the file
f.close()           #closes the file
f=open("text.txt","r")  #explicitly opening file in read mode
content=f.read(10)      #reads first 10 characters of the file
print(content)
f.close()
f=open("text.txt","r")
lines=f.readlines()     #reads all lines of the file into a list
print(lines, type(lines))  #prints the list of lines and its type ie. list
f.close()
f=open("text.txt","r")
for line in f:         #iterating through each line in the file
    print(line.strip()) #printing each line after stripping leading/trailing whitespace 
f.close()
f=open("output.txt","w")  #opens (or creates) file in write mode
f.write("This is a new line.\n")  #writes a line to the file
f.write("Writing to files in Python is easy!\n")
f.close()
f=open("output.txt","a")  #opens file in append mode
f.write("Appending a new line.\n")  #appends a line to the file
f.close()
line2=f.readline()  #reads a single line from the file
print(line2, type(line2))  #prints the line and its type ie. str


while(f.readline()!=""):  #reads lines until end of file
   print(f.readline()) #prints each line
f.close()

# Using 'with' statement to handle files (automatically closes the file)
with open("text.txt") as f:
    content=f.read()
    print(content) 
    #file is automatically closed after the with block
    #no need to explicitly call f.close()
