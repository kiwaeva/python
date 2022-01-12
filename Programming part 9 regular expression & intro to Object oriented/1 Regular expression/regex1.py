# Regular expressions are patterns that help a user match character combinations 
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.
#  Import the re module:

import re # import the module

"""\w = any alpha numeric char(any digits/character) = A-Z. Returns a match if the string 
contains alphanumeric characters including underscores. 
For example, \w will match a, b, c, d, 1, 2, 3, etc."""

# text/string to search
sentence = "Take up one idea, One idea at a time"
#find all substring within the given string above

#use search method to define search parameter and assign it to a variable
# used r to indicate regex search, then the first letter of the word to search for and as many \w\w as needed.
searchResult = re.search(r'o\w\w',sentence)

# group is a method on the result that comes back which will give us the exact string that matches
# the given pattern
print(searchResult.group())

# exercise
# searc for a four letter sub string that starts
# with i

searchResult = re.search(r'i\w\w\w',sentence)
print(searchResult.group())

