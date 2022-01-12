# not handling errors 
name = input("enter your name: ")
print(nama)
print("how are you today")

# handling the error with errors
try: # check for error
    name = input("enter your name: ")
    print(nama)
except NameError: # executed when there is error
    print("Name is not defined")
print("how are you today")
