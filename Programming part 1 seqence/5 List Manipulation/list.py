list1 = [] #declare list1 var and assign to it a list datatype
list2 = ["HTML","CSS"]

print(list1)

list1.append("Bootcamp") # use append to add item to the list
print(list1)

list2.append("Bootcamp")
print(list2)

list2.insert(0, "Python") #use the insert funct to insert item to a specific index position
print(list2)

#access list items by their index position
list3 =["Paul","Kate","Anna",1,2,34.7,-8]
print(list3[1])

#splicing a list
print(list3[1:2]) #only Kate
print(list3[1:3]) #Kate and Anna

#return the length of the list
print("The length of the list is:", len(list3))

#remove list items as per index position
print(list3)
del(list3[3])
print(list3)
del(list3[3], list3[4])
print(list3)
#remove list items as per item value
print(list3)
list3.remove("Kate")
print(list3)

# max and min function
list4 = [1,2,34.7,-8]
#return the min item from the list
print(min(list4))

#return max item from the list
list4 = [ 1, 2, 34.7, -8 ]
# return the minimum item from the list
print(min(list4))

# return the maximum item from the list
print(max(list4))

# sort list items
list4.sort() # sort list in ascending order
print(list4)

list4.sort(reverse=True)# sort list in descending order
print(list4)

# clear list
list4.clear() # clear/ remove all list items
print(list4)


#EXERCISE

# create a list of 6 items
# insert a new item in postion 3
# add another item to the list
# remove an item by value
# remove the item at index position 3
# for every list manipulation print the list

list5= ["Eve",20, 25.4, 50,-140]
list5.insert(3, "PythonLesson")
print(list5)

list5.append("JustIT")
print(list5)

print(list5)
list5.remove("Eve")
print(list5)


del(list5[3])
print(list5)