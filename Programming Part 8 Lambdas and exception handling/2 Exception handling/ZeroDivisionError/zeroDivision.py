# num1=int(input("Enter a num"))
# num2=int(input("Enter a num"))

# num1=12
# num2=0
# num3=num1/num2
# print(num3)

try:
    # num1=12
    # num2=0
    num1=int(input("Enter a num"))
    num2=int(input("Enter a num"))
    num3=num1/num2
    print(num3)
except ZeroDivisionError:
    print("You cannot devide a num by zero \nenter a num that is not 0")
finally:
    print("Closing the program")