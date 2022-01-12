#Task1:
# Write a new program which will create a list with 10 city names.
# • Print the list with all the items showing on one line.
cities = ["Riga","Vilnus","Berlin","London","Paris","Rome","Milan","Jurmala","Southampton", "Bournemouth"]
print(cities)
# • Insert a new city in index position 4
cities.insert(4,"Malaga")
print(cities)
# • Print out the fourth item in the list by it index position.
print(cities[3])
# • Print out the sixth item in the list by its value.
print("Rome")
# • Remove any two cities from the list
print(cities)
del(cities[8],cities[8])
print(cities)
# • How can you print the 4 th ,5 th ,6 th and 7 th cities in the list
print(cities[3:7])
# • Return the length of the list
print(len(cities))
# • Sort the list in ascending order
cities.sort()
print(cities)
# • Sort the list in descending order
cities.sort(reverse=True)
print(cities)
# Note: for every list manipulation print the list

#Task2
# You have been provided with the following string of characters stored in the variable as shown below
# userString = &quot; Python is my third programming language&quot;
uSt = "Python is my third programming language"
# • Print the 1st, 3rd, 6th, 9th and 11th characters from the string (userString) provided above.
print(uSt[0],uSt[2],uSt[5],uSt[8],uSt[10])
# • Return the length of the string
print(len(uSt))
# • Slice the string to print between the 3rd and 11 characters
print(uSt[3:12])
# • Omit the last and then second to last characters from your string in your print out
print(uSt[37:])
# • Print up to the 15 character from your string.
print(uSt[:16])
# • Find the start index position of the substring “third”
print(uSt.find("third"))
# • Print out the string in all capital letters.
print("Upper case: ",uSt.upper())
# • Print out the string in all non lower case letters.
print("Lower case: ",uSt.lower())
# • Print out the first letter of all the sub strings in capital letters.
print("Title case: ",uSt.title())
# • Replace the substring “third” to so that the string will reflect if it is your first or second…etc
print(uSt.replace("third", "fourth"))

#Task3 
# Write a program that will ask the user for how many sweets are in the bag.  
sweets = int(input("How many sweets are in the bag: "))
# •	It should also ask how many people the sweets should be shared between.
people = int(input("Between how many people it has to be shared: "))  
# •	Use the whole number division to work out how many sweets each person should have and use the remainder division to find out how many sweets would be left remaining.  
answer = sweets//people
print("Each person will get",answer, "sweets")
left= sweets%people
print("There will be",left,"sweets left")
# •	For example if there are 14 sweets in the bag and this was to be divided between 3 people then the programme should display “There will be 4 sweets each and there would be 2 left over.”

#Task 4

import random

#Homework4: use if else
#to print out if a double is thrown 
#to print out if a double is not thrown 

die1= random.randint(1,6)
die2= random.randint(1,6)

if die1==die2:
    print(die1,die2,"Start the game!")
else:
    print(die1, die2,"Try again!")

#Task5
# Modify your code in task 4:  
# •	To ask for one user input between 1 and 10
userinp = int(input("Enter number between 1 and 10: "))
inp = random.randint(1,10)
# •	Compare the user input with the random generated number
# •	Print out if a double is thrown
if userinp == inp:
    print("Well done!")
else:
    print("Try one more time :)")
# •	Print out if a double is not thrown


     




