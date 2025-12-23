#dictionary is a collection which is unordered, changeable, indexed and cannot contain duplicate keys. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

# Create and print a dictionary:
dict = {
           "brand": "Ford",
           "model": "Mustang",
           "year": 1964
           }
print(dict,type(dict)) #print both dictionary and its type together
print(len(dict))  #length of dictionary

# Accessing items
print(dict["brand"])  #using key
print(dict.get("model"))  #using get() method

# dictionaory items
print(dict.keys())  #printing all keys
print(dict.values())  #printing all values
print(dict.items())  #printing all key-value pairs
dict.clear()  #clearing the dictionary
dict.update({"color": "red"})  #adding new key-value pair
dict.update({"year": 2020})  #updating existing key-value pair
print(dict.get("brand")) #may return None if key not found
print(dict["brand"]) #this will raise an error if key not found
dict2 = dict.copy()  #copying the dictionary
dict.pop("model")  #removing an item with specified key
dict.popitem()  #removing the last inserted item

#set is a collection of well defined unique elements which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
# *Note: Set items are unchangeable, but you can remove items and add new items in the removed item's place.
# venn diagram representation of sets

s={"apple", "banana", "cherry",332,44.5,True}  #creating a set with different data types
set2={1,2,3,4,5}  #creating another set 

print(s,type(s))  #printing set and its type
print(len(s))  #length of set
print(type(s))  #type of set
print("banana" in s)  #checking if an item exists in set
s.add("orange")  #adding an item to set
s.update(["mango", "grapes"])  #adding multiple items to set
s.remove("banana")  #removing an item, raises error if item not found
s.discard("banana")  #removing an item, does not raise error if item not found
s.pop()  #removing a random item
s.clear()  #clearing the set
set2 = s.copy()  #copying the set
set3 = s.union(set2)  #joining two sets
set4 = s.intersection(set2)  #finding common items between two sets
set5 = s.difference(set2)  #finding items in set s that are not in set2
set6 = set2.symmetric_difference(s)  #finding items in either set but not in both
set7 = s.isdisjoint(set2)  #checking if two sets have no items in common
set8 = s.issubset(set2)  #checking if set s is a
set9 = s.issuperset(set2)  #checking if set s contains all items of set2
set10 = s.intersection_update(set2)  #updating set s to keep only items found in both sets
set11 = s.difference_update(set2)  #updating set s to remove items
set12 = s.symmetric_difference_update(set2)  #updating set s to keep only items found in either set, but not in both

e=set()  #creating an empty set
# e={}  #this will create an empty dictionary, not a set

set={2,3,4,5,6,6,6,7}  #creating a set with duplicate values
print(set)  #printing the set will show only unique values ie. {2,3,4,5,6,7}

#frozen set is a type of set that is immutable, meaning that once it is created, its elements cannot be changed, added, or removed.
fs=frozenset([1,2,3,4,5])  #creating a frozenset
print(fs,type(fs))  #printing frozenset and its type
print(len(fs))  #length of frozenset
print(3 in fs)  #checking if an item exists in frozenset    

# set is unordered, so items may appear in a different order every time you run the code.
# for ordered collections like lists or tuples maintain the order of items as they were added.
# cannot acces index of set items