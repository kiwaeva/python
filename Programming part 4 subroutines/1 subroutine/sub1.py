#subroutine:A sequence of instructions to perform a specific task with an identifiable name.
# def is a keyword used define a subroutine, followed by the name of the subroutine

# def username():
#     name= input("Enter your name: ")
#     print("Thanks fir joinin us",name)

# username() # call the subroutine locally inside it's own file.

#Exercice 1 : create subroutine 
# ask for firstname, last name, age and favourite movie
#call subroutine locally
#call subroutine in another file

def user():
    fname= input("Enter your name: ")
    lname= input("Enter your last name: ")
    fmovie= input("Enter your favourite movie: ")
    print(fname, lname, fmovie )
#user()