#selection is used to control the flow of the program 

# Comparison operator compare values
# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to 
# >= 	greater than or equal to
# !=    Not equal to

pstudy1 = input ("Enter your program of study:")

if pstudy1 == "Bootcamp": #equality operator to compare user input with value Bootcamp 
    print("Welcome to", pstudy1)# will be printed if condition is met on line 13
else: #execute if the condition on line 13 is not met
    print("Please enquire about our program of study")

# not equal operator

pstudy2 = input ("Enter your program of study:")

if pstudy2 != "Bootcamp": #equality operator to compare user input with value Bootcamp 
    print("Please enquire about our program of study")# will be printed if condition is met on line 13
else: #execute if the condition on line 13 is not met
    print("Welcome to", pstudy2)

# Exercise 1 : use the equality and not equal to operators 
# To check if the user enter their first name as your firstname
# Print out a message when the condition(firname = your firstname) is met or not met

firstName= input ("Enter your first name:")

if firstName == "Name":
    print("Welcome to the platform",firstName)
else:
    print("Please introduce yourself")

## with not eql operator

firstName1= input ("Enter your first name:")

if firstName1 != "":
    print("Please introduce yourself")
else:
    print("Welcome to the platform",firstName1)