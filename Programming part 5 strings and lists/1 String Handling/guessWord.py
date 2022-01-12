varWord = "sandwich"
# print(varWord)
user_guess = ""
not_guessed = varWord != user_guess
guesses = 0

while not_guessed and guesses <5: # check to make sure the number of not guessed and gueses is below 5, then do something
    if guesses == 1: # check if the no of guess is 1 
        firstLetter = varWord[0]
        print("Hint, the first letter of the word is: ", firstLetter)
    elif guesses == 3:
        lastLetter = varWord[7]
        print("Hint, the last letter of the word is: ", lastLetter)
    # print("Guess the word")
    user_guess = input("Guess the word: ")
    guesses = guesses + 1
    not_guessed = varWord != user_guess

if varWord == user_guess:
    print("You guessed right")
else: 
    print("incorrect...guess")
