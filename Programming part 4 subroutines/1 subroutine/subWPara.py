def addNums(value1, value2,value3): # param used in a subroutine to allow values to be passed into them.
    answer= value1+value2+value3 # create answer var to store the result of the addition
    print("The answer is:", answer)
#     # inside of the subroutine


# #Arguements: are The values held in the brackets of a subroutine call.
# #These  are passed intp a subroutine via the parametrs.
num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
num3 = int(input("Enter third num: "))

addNums(num1,num2,num3) #passed var as an arguement

addNums(200,300,12) #passed hardcoded/static num values as an arguement

addNums("Paul","Anna","James")

#Exercise 3 (With parameters)
#create a subroutine to  either  subtact, divide or multiply 
# Ask for two numbers
# evaluate the two numbers/ add two arguments 
# display the answer

def multNums(a, b):
    answer=a*b
    print("Answer is:",answer)

num_a=int(input("Enter num a: "))
num_b=int(input("Enter numb b: "))

multNums(num_a,num_b)