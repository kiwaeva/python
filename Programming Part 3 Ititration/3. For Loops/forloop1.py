# Iteration means repetition
# A for loop is another tool to control the flow of execution in your programs. 
# for loops is used when you have definite iteration 
# (the number of iterations is known).
import time

#number of iteration specified as 10 as argument in the range
#function, counting 10 items starting from zero
for number in range(11):
    print(number)


for number in range(5,15): #(start,end value) last number never included if you want 15 type 16
    print("With start and stop Values:")
    print(number)

for number in range(5,50,10):
    print("With start, stop and step Values:")
    print(number)

for number in range (5,16):
    time.sleep(1)
    print("with start, stop values")
    print(number)

for number in range (5,50,10):
    time.sleep(1)
    print("with start, stop and step values")
    print(number)


# Exercise 1
# Create timer that will count up to 50
# Increase the count by 1 every second
# Specify the start value to be 1
# Ensure the count include the number 50 as the end value

for number in range (1,51):
    time.sleep(1)
    print(number)