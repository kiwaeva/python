def alphabetList (): #create function
    alphaList=[] # create an empty list
    for letters in range(65,91): #specify the start and the end values to be itirated over
        alphaList.append(chr(letters)) # append/add the converted values to the list
    return alphaList

print(alphabetList())

print(bin(21))
