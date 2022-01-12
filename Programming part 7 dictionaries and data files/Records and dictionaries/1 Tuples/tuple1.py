tpl1 = (40,20, 30, 25) # declare a tuple with round brackets

bool1 = True
tpl2 = (40,20, 30, 25, 12.5, "Amy", "Orange", bool1)# tuple can hold items/values of different data types

print(type(tpl1)) # check the datatype

print(type(tpl2))


print(tpl1)
print(tpl2)

print(tpl2[4])# accessing item in a tuple by index position

print(tpl1.index(30)) # returns the index position of a value in the tuple

#exercise return the min and max item form tpl1

print("Max", max(tpl1))
print("Min", min(tpl1))

tpl3=(500,) #insure theres a come even if ther is one item in your tuple
print(type(tpl3))
