varWords = "This is python bootcamp"
count=0
varChar= input("Enter a character to search for:")

for aLetter in varWords: # aLetter is a var thet will iterate over the varWords and stor each character
    if aLetter == varChar: # aLetter will compare each char in varWords with char enter in varChar
        count= count +1  #count the char and increase by 1, if more than 1
        print("The character", varChar, "appears", count, "times")
else:
    print("The character is not found")