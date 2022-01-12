# Regular expressions are patterns that help a user match character combinations 
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.
#  Import the re module:

import re # import the module
"""\d  = 0-9 , \D = non digit characters, \s =white space , \S = non white space,
Matches the preceding character one or more times. 
The working of the + character is similar to *, but the + 
character omits the pattern if the character doesn't occur. 
For example, abc+ will match abc, abcc, abccc, etc. but not ab.

"""
# text/string to search
sentence = "Take up one2idea, One1idea at a 4 time"
''' The split method, splits the given string into a list of strings using the given RegEx 
passed as a limiter'''

#use search method to define search parameter and assign it to a variable
# used r to indicate regex search, then the first letter of the word to search for and as many \w\w as needed.
searchResult  = re.split(r'\d', sentence)

print(searchResult)
#exercise find the the white spaces in the string
searchResult= (re.split(r"\s",sentence))
print(searchResult)

#the amount of white spaces
searchResult= len(re.split(r"\s",sentence))
print(searchResult)