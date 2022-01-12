from guizero import App, Text, TextBox, PushButton

# create an instance object app from the App class
app = App(title="Addition", bg="cadetblue") # pass in arguments to give our gui a title and a background colour

# created a variable to instruct the user to enter an input using the text class
instruction1 = Text(app, text="Enter first number: ")

# created a variable for the user to enter an input/value using the textbox class
enterNum1 = TextBox(app)

instruction2 = Text(app, text="Enter second number: ")
enterNum2 = TextBox(app)

# created a variable to display the answer using the text class
displayAnswer = Text(app, text="Answer will be displayed here")

def addition():
# created two local variables num1/num2 to pass the values entered into the texboxes enterNum1/enterNum2 
    num1 = enterNum1.value # the .value proerty to capture input entered in the textboxes
    num2 = enterNum2.value
# created local variable answer to store  total / convert num1 and num2 to interger data type
    answer = int(num1) + int(num2)
    displayAnswer.value = answer

# created an instance object using the variable calcButton from the PushButton class 
# pass in the app, command and text arguments with their respective values 
calcButton = PushButton(app, command=addition, text="Add")

app.display()