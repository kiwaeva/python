globalVar = 20  #"global Var", 

print(globalVar)


globalVar= 10 #"global Var", 
print("Global Var", globalVar)  


def localVar():
    globalVar = 1 # local variable
    return globalVar


print(globalVar) 

testLocal = localVar()

print("Local Var", testLocal)
