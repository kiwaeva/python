#Selection is used to control the flow of the program

# Comparison operator compare values
# == equal 
# < 	less than
# > 	more than/greater than
# <= 	less than or equal to 
# >= 	greater than or equal to
# !=    Not equal to 

# use of and operator with selection
cardValue = input("Enter a card value: ")
suitOfCards = input("Enter a card suit: ")

if cardValue == "King" and suitOfCards =="hearts":
    print("Your card is a match")
else:
    print("Your card is not a match")

# use of or operator with selection
cardValue = int(input("Enter a card number: "))
suitOfCards = input("Enter a card suit: ")

if cardValue <7  or  suitOfCards =="spades":
    print("Your card is a match")
else:
    print("Your card is not a match")