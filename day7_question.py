#print multiplication table of a given number using for loop
'''
n=int(input('enter n'))
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')
'''

# greet all the person names stored in a list 'l' and which starts with S. 
'''
l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if(name.startswith("S")):
        print(f"Hola {name}")
'''

'''
   *
  ***
 *****
'''

'''
n=3
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'* ((2*i)-1),end='') #end='' used for not letting python add new line as default
    print('\n')
'''