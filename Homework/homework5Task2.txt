# chr(): takes a decimal and returns the ascii equivalent
# ord(): takes a character and returns the decimal equivalent

varMsg = ""
varLetter = input("Enter a single character tha is not a number: ")
varConvert = ord(varLetter)
varMsg = varMsg + str(varConvert)
print(varMsg)
