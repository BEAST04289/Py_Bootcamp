# store seven fruits in a list entered by the user
fruits = []
f1=input("Enter fruit 1: ")
fruits.append(f1)
f2=input("Enter fruit 2: ")
fruits.append(f2)
f3=input("Enter fruit 3: ")
fruits.append(f3)
f4=input("Enter fruit 4: ")
fruits.append(f4)
f5=input("Enter fruit 5: ")
fruits.append(f5)
f6=input("Enter fruit 6: ")
fruits.append(f6)
f7=input("Enter fruit 7: ")
fruits.append(f7)
print("Fruits entered:", fruits)

# sum a list with 4 numbers
numbers = []
n1 = float(input("Enter number 1: "))
numbers.append(n1)
n2 = float(input("Enter number 2: "))
numbers.append(n2)
n3 = float(input("Enter number 3: "))
numbers.append(n3)
n4 = float(input("Enter number 4: "))
numbers.append(n4)
total = sum(numbers)
print("Sum of the numbers:", total)

# count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9) 

a = (7, 0, 8, 0, 0, 9)
zero_count = a.count(0)
print("Number of zeros in the tuple:", zero_count)