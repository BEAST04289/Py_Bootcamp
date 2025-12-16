# display a user entered name followed by Good Afternoon using input () function
name=input("Enter Your Name")
print(f"Good Afternoon, {name}!!")

# fill in a letter template given below with name and date
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|>
'''
#chaining- it changes the change in the new string
print(letter.replace('<|Name|>','Shaurya').replace('<|Date|>','18 dec 2026'))

# detect double space in a string
space='hii  there'
print(space.find('  ')) # gives index where its starts from


# Replace the double space from problem 3 with single spaces
print(space.replace('  ','   '))

#format the following letter using escape sequence characters. 
# letter = "Dear Harry, this python course is nice. Thanks!" 
letter = "Dear Shaurya, \nthis python course is nice.\nThanks!"
print(letter)

