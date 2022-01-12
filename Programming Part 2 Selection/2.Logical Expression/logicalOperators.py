# Comparison operator compare values
# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to 
# >= 	greater than or equal to
# !=    Not equal to

#Logical expressions evaluate to true or false
#Logical operators: and,or, not 

num1 = 15 #use assignment operator(=) to assign 15 to num1 var
num2 = 20 #use assignment operator(=) to assign 20 to num1 var

print((num1==15 and num2==20)) #returns true as both sides equasions eqates to true
print((num1==135 and num2==20)) #returns false as one side of equasions not eqates to true

#Exercise1: use the OR operator to return an equation that equates to true
num3=30
num4=50

print((num3==35 or num4==50)) # if one or more of equations equates to true then it's true
print((num3==35 or num4==50)) # if both of equations do not equate to true then it's false

#Exercise2: use the Not operator to return an equation that equates to True
print(not(num3==35 or num4==40))
print(not(num3==35 and num4==50))

#Exercise3: use the Not operator to return an equation that equates to true and false
print(not(num3==35 or num4==40))
print(not(num3==30 or num4==40))

