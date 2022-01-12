# A lambda is simply a way to define a function in Python. They are sometimes known as "lambda 
# operators" or "lambda functions".  A lambda function is a small anonymous function, they are functions
# that don't need to be named. They are used to create small, one-off functions in cases where a "real "
# function would be too big and bulky.   A lambda function can take any number of arguments, but can 
# only have one expression. lambda arguments : expression .

# Lambdas return a function object, which can be assigned to a variable. Lambdas can have any number
#  of arguments, but they can only have one expression. You cannot call other functions inside lambdas.

"lambdaarguements: expression"

#variable = lambda parametr
addTwoNums = lambda num: num + 10
print(addTwoNums(2)) # the num two is the arguement that gets passed into the parametr

sumOfNums = lambda num1,num2: num1+num2
print(sumOfNums(5,11))

#exercise 
# perform multiplication with one parameter and  one argument
# perform multiplication with two parameters and two arguments
# perform multiplication with three parameters and three arguments

oneNum= lambda num: num*10
print(oneNum(2))

twoNums= lambda num1,num2: num1*num2+10/2
print(twoNums(5,7))

threeNums= lambda num1,num2,num3: num1*num2*num3-2/2
print(threeNums(1,2,3))


# ~exercise modify program below to ask user to input number
addTwoNums =  lambda num: num + 10  # the expression is num + 10 

print(addTwoNums(int(input("Enter number: "))))


#someone elses solution
x3 = int(input("Enter a number 1-10: "))
y3 = int(input("Enter another number 1-10: "))

multiNums2 = lambda x3, y3: x3 - y3 
print(multiNums2(x3, y3))
