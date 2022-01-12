# In order to read the data stored in a text file, you must open it first. 
# Just like a book. You can’t read what is inside if you don’t open it first.
# There are four modes for opening a file:
# r	for only reading files
# w	for only writing to files
# a	for adding to an existing file

file1= open("ReadWrite/notes1.txt","r") 
readfile = file1.read()
print(readfile)
