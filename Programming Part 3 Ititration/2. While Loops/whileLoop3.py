num1=1
while(num1 <= 20):
    print(num1)
    num1+=1 #increment the num1 value by 1


    # exercise 1
# write a program that will ask he user to guess your firstname
# continue to ask the user if they dont guess your name correctly
#print out your name when the user guessed it correctly and end the program

#exercise 2
# write a prgram that ask the user for a number below 5
#count from the number the user entered to 25
# print the count

firstName = input("Guess my first name: ")

while firstName != "Evelina":
    firstName = input("Try again ;) ")
print("Well Done!You guessed right!", firstName)


num = int(input("Type a number that is less than 5: "))
while (num <= 25):
    print(num)
    num+=1

