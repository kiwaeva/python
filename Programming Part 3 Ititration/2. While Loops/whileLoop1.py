#The while loop keeps going until the condition is met


guessWord = input("Guess a word: ")
while guessWord != "python":
    guessWord = input("Try again to guess a word: ")
print("Well Done!You guessed right!", guessWord)
