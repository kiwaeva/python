#When a selection block (if/else) is places within another statement block is called a nested selection


userAge= int(input("Enter your age:"))
if userAge >16:
    #will execute if condition on line 5 is met
    course = int(input("Enter the number of courses you are enrolled on:"))
    if course > 2:
        print("Emoressive, you enrolled on",course,"courses")
    else: #will execute if condition on line 8 is not met
        print("You should enrol on more courses")
else: #will execute if condition on line 5 is not met
    print("Hope you'll enrole on more courses when you turn 17")

