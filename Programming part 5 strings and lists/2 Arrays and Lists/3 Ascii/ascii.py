# chr(): takes a decimal and returns the ascii equivalent
# ord(): takes a character and returns the decimal equivalent

varMsg = ""

varNum = int(input("Enter a number: "))
varConvert = chr(varNum)
varMsg = varMsg + varConvert

print(varMsg)