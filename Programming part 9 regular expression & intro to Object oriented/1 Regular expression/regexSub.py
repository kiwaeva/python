#  Import the re module:

import re # import the module



# text/string to search
sentence = "Take up one2idea, One1idea at a 4 time one open old older olga"

''' The sub method, substitute the given string with a new string using the given RegEx 
format passed in'''''

#use search method to define search parameter and assign it to a variable

# second parameter specified inthe sub function replaces the first parameter 
searchResult  = re.sub(r'one', 'two', sentence)
print(searchResult)


#exercise substitute any substring that start with the letter regardless of the num of characters that follows after

searchResult = re.sub(r'T\w+','Make',sentence)
print(searchResult)

#findall function

searchResult = re.findall(r'o\w\w',sentence) #find substring with 3 characters that starts with o
print(searchResult)

searchResult = re.findall(r'o\w+',sentence) #find substring with 3 characters that starts with o
print(searchResult)