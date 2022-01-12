# A subroutine:A sequence of instructions to perform a specific task with an identifiable name.
# A function is a type of subroutine that returns a value

def addNumbers():
    num1=10
    num2=20
    answer= num1+num2
    return answer # A value is returned by a function

print(addNumbers()) # call the addNumbers funct in the print statement

functAnswer= addNumbers() #assign the function to a variable 

print("The answer is: ", functAnswer)

#Exercise: modify the addNumbers function to add parametrs and arguements

def addNum():
    answer=int(input("add num: "))
    return answer()
