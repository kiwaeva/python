import logging # import the logging library
# logging levels
logging.basicConfig(filename="Log4.log", level=logging.DEBUG) # set the minimum logging level 

try:
    file1 = open("FileLog.txt", "a") # open file and use ghe append flag "a"
    num1 = int(input(" enter a number "))
    num2 = int(input(" enter a number "))
    num3 = num1/num2
    file1.write(f"\nThe answer is {num3}") # writing tthe answer to the file
    logging.info("Division in progress")# logging that division is in progress
    # print(num3)
except ZeroDivisionError:
    errorMsg ="You can't divide a number by zero\nenter a number that is not zero" # passed string into a variable
    print(errorMsg)# print the sring held in the variable using the variable
    file1.write(errorMsg) # writing the error msg to file to the file
    logging.error("Divison by zero is not allowed")

finally:
    print("closing the program")
