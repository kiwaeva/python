#List is an ordered sequence of items. It is a very flexible data type in python
# The values in the list don't have to be of the same type
#ITEMS IN A LIST CAN BE MODIFIED
# declare a list1 var and assign val of different datatypes in the list 

list1 = [1,5,9.9, "list"]
list2 = [1,3,4,5,10,20]
print("\nThis is a list")
print(type(list1))
print(list1)
print(type(list2))
print(list2)

# Tuple is a sequence of items that are in order and they can't be modified 
# Tuples are faster than lists and the primary use of tuples are to create write protect data

#declare  tuple var and assign val of different datatypes in tuple
tuple1 = (6, "tuple",-4,3.2)
print("\nThis is a tuple")
print(type(tuple1))
print(tuple1)

#Set is a collection of unique items that are not in order
#Duplicates are eliminated in a set
#Set items cannot be accessed based on their index position

#decl a set1 var and assign val of different datatypes in the set
set1= {4,5,5,10.5,"xyz",1.3,5,"xyz"}
print("\nThis is a set")
print(type(set1))
print(set1)
#outcomes
#duplicate items will be printed only once
# items in the set will be displayed in no particular order


# Dictionary
# to retrive a specific val from the dict you need to know the key

dictionary1 = {1:"John", 2:"Anna",3:"Peter"}
print("\nThis is a dictionary")
print(type(dictionary1))
print(dictionary1)