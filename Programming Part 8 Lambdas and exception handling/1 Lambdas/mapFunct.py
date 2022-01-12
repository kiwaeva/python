# The map function expects two arguments: a function and a list.
# It takes that function and applies it to every element in the list, 
# returning the list of modified elements as a map object. 
# The list function is used to convert the resulting map object back into a list again.

# declare a list of numbers

listofNums = [1,2,3,4,5,6,7,8,9,10,12,21,24,30,31]
listResult = list(map(lambda num: num+2, listofNums))
print(listResult)