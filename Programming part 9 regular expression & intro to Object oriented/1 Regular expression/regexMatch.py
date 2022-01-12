# Regular expressions are patterns that help a user match character combinations 
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.
#  Import the re module:

import re # import the module



# text/string to search
sentence = "Take up one2idea, One1idea o1234 at a oWN oWNer 4 time one open old older olga"
'''The RegEx Match method used, takes a regular expression 
and search for that pattern right at the beginning of the string '''

searchResult= re.match(r'T\w\w',sentence)#matches only the one at the start
# print(searchResult.group())
print(searchResult)
