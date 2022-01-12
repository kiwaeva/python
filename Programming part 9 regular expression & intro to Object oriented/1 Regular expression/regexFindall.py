# Regular expressions are patterns that help a user match character combinations
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.
#  Import the re module:

# " Matches the preceding character one or more times. The working of the + character
# is similar to *, but the + character omits the pattern if the character doesn't occur.
# For example, abc+ will match abc, abcc, abccc, etc. but not ab.

import re  # import the module
# findall function
'''' RegEx findall method searches a string from the beginning to the end of the string, and return all the sub-string 
that matches the given regular expression in a list and returns an empty list if no match is found. '''


sentence = "Take up one idea. One idea  at a ones once open o a time"

# searchResult = re.findall(
#     r'o\w\w', sentence)  # find substring with 3 characters that start with o
# print(searchResult)

# The "\w+"  is used to match one/more characters/digits after the character specified
searchResult = re.findall(r'o\w+', sentence)  # find substring with one or more characters that start with o
print(searchResult) # o followed by  1,2,3,4,5,6 characters

# * zero or more repetitions of the preceding RegEx (starting with the letter specified)
searchResult = re.findall(r'o\w*', sentence)  #
print(searchResult)  # o followed by no character/digits  or 1,2,3,4,5,6 characters

# The question mark "?" RegEx use to match zero or one repetition of alpha numeric characters starting with letter o
searchResult = re.findall(r'o\w?', sentence)  #
print(searchResult)  # o followed by no character/digits  or 1,2,3,4,5,6 characters


# exercise find three characters after the letter o, using the curly braces with oone value inside
searchResult = re.findall(r'o\w', sentence)  #
print(searchResult)  # o followed by no character/digits  or 1,2,3,4,5,6 characters

# exercise find 1 or 2 characters after the letter o, using the curly braces with two values inside
searchResult = re.findall(r'o\w', sentence)  #
print(searchResult)  # o followed by no character/digits  or 1,2,3,4,5,6 characters
