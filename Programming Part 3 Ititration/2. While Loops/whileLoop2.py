# The While loop keeps going until the condition is met (unknown number of times). 

userPassword = input("Enter password: ")

passwordAttempts = 2 # create a flag variable ad set the value to 2

while userPassword != "python" and passwordAttempts <3:
    userPassword = input("Re-enter password: ")
    passwordAttempts+=1 # increase password attemp by 1
if userPassword =="python": # check input value with value python
    print("Password valid")# execute if condition on line 10 is met
else:
    print("Password Rejected")
