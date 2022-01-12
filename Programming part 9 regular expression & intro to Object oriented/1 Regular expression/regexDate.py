# Regular expressions are patterns that help a user match character combinations 
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.
#  Import the re module:

import re # import the module

# \d  = 0-9 , \D = non digit characters, \s =white space , \S = non white space,

# text/string to search
sentence = "Taken up Two 02-12-2021  one Too  2idea,  2-12-2021 Tame ne1idea o1234 at a  2-12-21 oWN oWNer 4 time one open old older olga"

''' Use findall method to quantify to match multiple characters, example plus sign (+) to 
specify one or more repetitions of the preceding RegEX'''

# The curly braces "{}" RegEx use to specify a minimum and maximum 
# number of occurrences of the preceding RegEX  {min, max}'''

searchResult = re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}', sentence)

print(searchResult)
