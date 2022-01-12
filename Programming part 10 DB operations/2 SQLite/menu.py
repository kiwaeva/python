from readMembers import *
from addmembers import *
from updateMembers import *
from deletemembers import *

#create a function with menu options
def menuOptions():
    options = 0
    #check for the value zero in the list
    while options not in ["1","2","3","4","5"]:
        print("nMenu Options")
        print("1. Print Members details")
        print("2. Add a new member")
        print("3. Update member details")
        print("4. Delete a member")
        print("5. Exit")
        options= input("\n Enter one of the options above: ")
        if options not in ["1","2","3","4","5"]:
            print("Not in the list of the options")
        return options

#create a var with a boolean value set to True
mainProgram= True

while mainProgram == True:
    #pass menuOptions funct to the var mainMenu which will display the menu option
    mainMenu = menuOptions()

    if mainMenu == "1" :
        showRecords()
    elif mainMenu == "2":
        addMembers()
    elif mainMenu == "3":
        update()
    elif mainMenu == "4":
        delRecord()
    else:
        mainProgram = False
    input("Press enter to exit")


# menuOptions()