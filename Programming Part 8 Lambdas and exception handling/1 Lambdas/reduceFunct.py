from functools import reduce
# Reduce is another cool Python function. 
# It applies a rolling calculation to all 
# items in a list. You could use this to tally
#  up a sum total, or multiply all numbers together:

# declare a list of numbers

# listofNums = [1,2,3,4,5,6,7,8,9,10,12,21,24,30,31]
listofNums = [1,2,3,4]

lstResults = reduce(lambda num1,num2: num1 + num2, listofNums)

print(lstResults)
