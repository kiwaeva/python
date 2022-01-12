# sets are used to store multiple items in a single variable..
# Set Items: Set items are unordered, unchangeable, and do not allow 
# duplicate values.



set1 = {40,20, 30, 25, 20, 21}
print(type(set1)) #check the type 
print(set1)# print items in the set

set2 = {1,2,34}
print("before update",set2)


set2.update([10,14,21,32,6])
print("after update",set2)

# frozen set

fset2  = frozenset(set2) #created a frozen set using the frozenset function
print("Set2 is frozen",fset2)


# fset2.update([10,14,21,32,6])
# print("attemp to update frozen set",fset2)

# create a set 
# update the set 
# prevetn the set from been update
 
set5={11,20,"Anna"}
print(set5)

set5.update(["Mike", 13,28])
print("Updated set", set5)

fset5=frozenset(set5)
print("Set5 is frozen",fset5)