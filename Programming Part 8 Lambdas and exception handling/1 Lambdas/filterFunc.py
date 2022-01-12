# With the filter function, the process is much the same. 
# Filter takes a function and applies it to every element 
# in a list and created a new list with only the elements 
# that caused the function to return True.

listofNums = [1,2,3,4,5,6,7,8,9,10,12,21,24,30,31]
listResults= list(filter(lambda num: num%2==0,listofNums))
print("These are even nums from the list",listResults)

listResults2= list(filter(lambda num: num%2!=0,listofNums))
print("These are off nums from the list",listResults2)

for evenNums in listResults:
    print(evenNums)

print("The amount of even numbers",len(listResults))
print("The amount of odd numbers",len(listResults2))