#Exercise: modify the addNumbers function to add parametrs and arguements

#whatever is passed inside the brackets of the function when the funct is created is a parametr 
def addNum(a,b): #defining function and givin it a name
    answer= a+b #using parametr as a place to perform addition 
    return answer

#whatever is passed inside the fucnction brackets when the function is called is an arguement
solution= addNum(10, 12)
solution2=addNum(23,13)

num1=int(input("Enter a num: "))
num2=int(input("Enter a num: "))

solution3= addNum(num1,num2)

print("The answer is: ", solution3)