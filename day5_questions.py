 # create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

words={
    "kal":"yesterday",
    "paani":"water",
    "dost":"friend",
}

word=input("Enter a Hindi word to look up its English translation: ")

print(words[word])

# input eight numbers from the user and display all the unique numbers (once). 

numbers=set()
for i in range(8):
    num=int(input("Enter a number: ")) #input as integer
    numbers.add(int(num)) #make sure to add as integer
print("The unique numbers are: ")
for number in numbers:
    print(number)

''' What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 
'''
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s)) # length will be 2 because 20 and 20.0 are considered the same in a set

'''  Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique. 
'''
fav_lang={}
for i in range(4):
    name=input("Enter your name: ")
    language=input("Enter your favorite programming language: ")
    fav_lang[name]=language

print("Favorite languages of friends:")
for name, language in fav_lang.items():
    print(f"{name}: {language}")