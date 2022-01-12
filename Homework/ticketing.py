
from datetime import date


def valid_integer():
    not_valid = True # not valid is a boolean datatype which is true
    while not_valid: # this while loop will be executed as the not_valid variable equates to true
        try: 
            number=int((input()))
            not_valid = False # not valid is a boolean datatype reset to false
        except ValueError:
            print("you must enter a number: ")
    return number

def entrance(child_total, adult_total, senior_total):
    total_cost= child_total * 12
    print(total_cost)
    total_cost= total_cost + adult_total * 20
    print(total_cost)
    total_cost=  total_cost + senior_total * 11
    print(total_cost)
    return total_cost

def parking():
    print("parking is free")
    required = input("Do your require parking: Enter Y or N").upper()
    while required != "Y" and required != "N":
        # print("You must enter Y or N")
        required = input("You must enter Y or N").upper()
    return required


def collect(total_cost):
    print("The total cost is" , total_cost)
    print("machine only accepst £10 and £20 Notes")
    amount_paid= 0 
    while total_cost > amount_paid:
        enterAmount = valid_integer()
        if enterAmount == 10:
            amount_paid = amount_paid + 10
        elif enterAmount  == 20:
            amount_paid = amount_paid + 20
        else:
            print("machine only accepst £10 and £20 Notes")
    if amount_paid > total_cost:
        change = amount_paid - total_cost
        print("Your change is: ", change)
        
def lead_surname():
    surname = input("Enter your surname")
    return surname


def issue_ticket(child_total, adult_total, senior_total, total_cost):
    print("entrance......")
    print(".....")
    today = date.today()
    print(" Your tickets are valid on:",  today)
    print(" Your Lead booker is:",  surname)
    print(" Your total adult ticket is :",  adult_total)
    print(" Your total  child ticket is:",  child_total)
    print(" Your total  senior ticket is:",  senior_total)
    print(" Your total  cost for all your tickets is:",  total_cost)



print("Welcome to bootcamp adventure Theme Park")
print(".........................................")
print("Entrance prices")
print("Adult........£20")
print("Child........£12")
print("Senior citizen.....£11")
print("........")
print("How many many adults tickets do you require?")
adult_total = valid_integer()
print("How many many child tickets do you require?")
child_total = valid_integer()
print("How many many senior citizen tickets do you require?")
senior_total = valid_integer()
total_cost = entrance(child_total, adult_total, senior_total)
surname = lead_surname()
collect(total_cost)
required = parking()
issue_ticket(child_total, adult_total, senior_total, total_cost)
if required == "Y":
    print("You have a car pass")
print("Enjoy you adventures")


