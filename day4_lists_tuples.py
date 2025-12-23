#lists are mutable whereas tuples and strings are immutable
my_list = [1, 2, 3,False, None, "hello"]
my_tuple = (1, 2, 3)
my_list[0] = "changed"
#my_tuple[0] = "changed" # this will raise an error 
print(my_list)
print(my_tuple)
print(type(my_list))
print(type(my_tuple))  
print(len(my_list))
print(len(my_tuple))
print(my_list[2])
print(my_tuple[2])
print(my_list[1:4])  #slicing works for both lists and tuples
print(my_tuple[1:3])
my_list.append("new item")  #adding an item to the list
print(my_list)
#my_tuple.append("new item")  #this will raise an error
my_list.remove(False)  #removing an item from the list  
print(my_list)
print(my_tuple.count(2))  #counting occurrences in a tuple
print(my_list.index("hello"))  #finding index of an item in a list
num=(213,324,64,87,12,45)
num.count(87)  #counting occurrences in a tuple
num.index(64)  #finding index of an item in a tuple
print(sorted(num))  #sorting a tuple (returns a list)   
print(num)  #original tuple remains unchanged
print(sorted(my_list, key=str))  #sorting a list with mixed types (as strings)
num2=[5,2,9,1]
num2.sort()  #sorting a list in place
num2.append(3) #adding a new item at the end
num2.insert(2,4) #inserting an item 4 at index 2
num2.remove(9) #removing an item
num2.reverse() #reversing the list
num2.pop() #removing and returning the last item
num2.extend([7,8,6]) #extending the list with another list
num2.clear() #clearing all items from the list
print(num2)
n=(1,) #single element tuple requires a comma
