# conditions in Python
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
# Output: x is positive
# You can also use nested conditions
y = 5
if x > 0:
    if y > 0:
        print("Both x and y are positive")
    else:
        print("x is positive but y is not positive")
# Output: Both x and y are positive
# You can use logical operators
if x > 0 and y > 0:
    print("x and y are both positive")  
# Output: x and y are both positive
if x > 0 or y < 0:
    print("At least one of x or y is positive")
# Output: At least one of x or y is positive
# You can use the 'not' operator
if not (x < 0):
    print("x is not negative")  
# Output: x is not negative
# You can use conditional expressions (ternary operator)
result = "x is positive" if x > 0 else "x is not positive"
print(result)
# Output: x is positive
# You can also combine multiple conditions
if (x > 0 and y > 0) or (x < 0 and y < 0):
    print("x and y have the same sign")
# Output: x and y have the same sign    
# You can use the 'in' keyword to check membership
numbers = [1, 2, 3, 4, 5]
if x in numbers:
    print("x is in the list of numbers")
# Output: x is in the list of numbers
# You can use the 'is' keyword to check identity
a = [1, 2, 3]
b = a
if a is b:
    print("a and b refer to the same object")
# Output: a and b refer to the same object

# You can use the 'pass' statement as a placeholder
if x > 0:
    pass  # Do nothing for now
    print("x is positive, but no action taken")
# Output: x is positive, but no action taken
# You can use the 'else' clause with loops
for i in range(3):
    print(i)
else:
    print("Loop completed")
# Output:
# 0
# 1
# 2
# Loop completed
# You can use the 'break' statement to exit loops   
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0     
# 1
# 2
# You can use the 'continue' statement to skip iterations
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output:
# 0
# 1
# 3
# 4
# You can use the 'while' loop with conditions
count = 0
while count < 3:
    print("Count is:", count)
    count += 1
# Output:
# Count is: 0
# Count is: 1
# Count is: 2

# You can use 'elif' for multiple conditions
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
# Output: Grade: B
# You can use nested 'if' statements
num = 15
if num > 0:
    if num % 2 == 0:
        print("num is a positive even number")
    else:
        print("num is a positive odd number")

# Output: num is a positive odd number

# You can use the 'all' and 'any' functions with conditions
values = [True, True, False]
if all(values):
    print("All values are True")    
else:
    print("Not all values are True")
# Output: Not all values are True
# Output: num is a positive odd number
# You can use the 'any' function
if any(values):
    print("At least one value is True") 

#while Output: At least one value is True
a=3
b=5
while a < b:
    print("a is less than b")
    a += 1  
# Output:
# a is less than b
# a is less than b

#for loops with else
for i in range(2):
    print("Iteration:", i)
else:
    print("Finished all iterations")
# Output:
# Iteration: 0  
# Iteration: 1
# Finished all iterations

