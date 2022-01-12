# number = int(input("Enter number:"))
# print("You entered:", number)


try:
    number = int(input("Enter number:"))
    print("You entered:", number)
except ValueError:
    print("Number is not defined")
    print("Please, try again")