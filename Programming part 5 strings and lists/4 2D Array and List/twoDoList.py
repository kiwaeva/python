

userScores = [["Paul","Anna","Lusy"],#row zero holds usernames
              [4     ,   5,    6],#row 1 holds user scores
              ["HTML", "CSS", "JS"] #row 2 holds user slills
] 
print(userScores[0])
print(userScores[0][1])

print(userScores[1])
print(userScores[1][1])

print(userScores[2])
print(userScores[2][1])

userScores[0].append("Tim") #append
userScores[0][1]= "Janet"
print(userScores[0])
