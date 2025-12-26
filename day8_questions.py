"""
read the text from a given file poems.txt and find out 
whether it contains the word twinkle.
"""
with open("poems.txt","r") as f:
    content = f.read()
    if "twinkle" in content:
        print("yes, the word twinkle is present in the file")
    else: 
        print("no, the word twinkle is not present in the file")

"""
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file Hi-score.txt which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score
"""
import random 

def game():
    print("you are playing a game")
    score = random.randint(1,11)

    with open("hiscore.txt","r") as f :
        hiscore=f.read()
        if(hiscore!=""):
            hiscore= int(hiscore)
        else:
            hiscore=0
    print(f"your score : {score}")
    if(score>hiscore):
         with open("hiscore.txt","w") as f :
             f.write(str(score)) #make sure its str as write function requires str

    return score

game()

"""
A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file
"""

word =["Donkey", "bad", "ugly", "stupid"]
with open("poems.txt","r") as f:
    content = f.read()
  
contentnew= content
for w in word:
    contentnew = contentnew.replace(w, "#"*len(word))
with open("poems.txt","w") as f:
    f.write(contentnew)



