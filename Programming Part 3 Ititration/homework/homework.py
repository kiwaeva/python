import time

#Task1

# for number in range (60,0,-1):
#     time.sleep(1)
#     print(number)

#Task2

# number = float("Enter decimal number: ")
# if number!= float:
#     print("Please enter decimal number")

#Task3

"""
Ask user to enter number to generate multiplication table
Add for loop with multiplyby var with value of numbers from 1 to 12 (12 INCLUDING)
Print user number multiplied by multyplyby numbers equal to num*multyplyby


"""

#Task4
#While loop will fun until condition is met
#For loop is used when you have definite iteration 
#example1
magicWord = input("Guess a magic word: ")
while magicWord != "abracadabra":
    magicWord = input("Try again to guess a magic word: ")
print("Well Done!You guessed it right!", magicWord)
#example2
import time
for num in range(21):
    time.sleep(1)
    print(num)

#Data validation is important so that Error message and instructions displayed are clear for the user 