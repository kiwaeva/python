class MobilePhone:
    def __init__(self,phoneMake, phoneDes, phoneModel, phonePrice ):
        self.make =   phoneMake 
        self.description = phoneDes
        self.model = phoneModel
        self.price = phonePrice 

mobilePhones  = []  

while True:
    addMobile = MobilePhone(       
            input("Enter phone make/brand: "),
            input("Enter phone description: "),
            input("Enter phone model: "),
            input("Enter phone price: ")
            )
    mobilePhones.append(addMobile.make +" "+ addMobile.description +" "+ addMobile.model+" "+addMobile.price)
    anotherMobile = input("Add another Mobile phone? Y/N").upper()
    if anotherMobile == "N":
        break
print(mobilePhones)
for mobile in mobilePhones:
    print(mobile)

