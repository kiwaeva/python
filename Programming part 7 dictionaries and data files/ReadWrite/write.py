# In order to read the data stored in a text file, you must open it first. 
# Just like a book. You can’t read what is inside if you don’t open it first.
# There are four modes for opening a file:
# r	for only reading files
# w	for only writing to files
# a	for adding to an existing file


file = open("ReadWrite/notes1.txt","a")
file.write("\n We are writing to this file")

# exercise append data to file
# existing data must not be deleted/replaced

user= input("Enter your name: ") #"James"
print(user)
#how can you pass captured user data to a file