mark= int(input("enter mark:"))

if mark >=75:
    grade="A"

elif mark >=60:
    grade="B"

elif mark >=50:
    grade="C"

else:
    grade="F"

print("You scored",mark,"and your grade is:",grade)