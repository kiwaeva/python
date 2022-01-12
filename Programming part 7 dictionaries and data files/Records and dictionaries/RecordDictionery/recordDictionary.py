# A record is a static data structure. You must determine the attributes and the data types for each entity
# during declaration. These will then be fixed for each record used in the database. Python does not have 
# a native data structure for a record.  data structure called a dictionary to represent a record.  A 
# dictionary has some of the features of a record.  
# A dictionary has key value pairs and is mutable in nature.  We use square brackets to declare a dictionary.


"Create a dictionary with key value pairs"
# A dictionary is a collection of records
dict1={1:"John",2:"Paul", 3:"Anna",4:"Lucy"}
print(type(dict1))
print("The items in the dictionaries are: ",dict1)

#print all items in the dictionary using the item method
print(dict1.items())

#print keys of items in a dictionary using the key method
dKeys = dict1.keys() #use the keys method 
for i in dKeys: #each key will be iterated over and stored in the var i
    print(i)

print(dict1[1])

#Exercise
#print out only the values using for loop
# use the example above as a guide
# use the values() method

dValues=dict1.values()
for a in dValues:
    print(a)



# ticket
#key                 value 
ticket = {"childticket":12, "adultticket":18, "seniorticket":11}
totalticket = {"totalchildticket":2, "Tadultticket":2, "Tseniorticket":1}

dKeys = ticket.keys() # declare a variable and use the keys method 
for i in dKeys: # each key will be iterated over and stored in the variable i
    print(i)


dVals = ticket.values() # declare a variable and use the keys method 
for i in dKeys: # each key will be iterated over and stored in the variable i
    print(i)
