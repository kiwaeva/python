

class MobilePhone: #outer/main class
    def __init__(self,phoneMake, phoneDes, phoneModel, phonePrice ):
        self.make =   phoneMake # "String Variable"
        self.description = phoneDes
        self.model = phoneModel
        self.price = phonePrice # 1234.7 = float data type

    #create methhod in a class
    def phoneDiscount(self): # method inside the outer class ony
        calcDiscount = self.price * 0.2  # 600 x 20% 
        discountPrice = self.price - calcDiscount # (phoneprice) 600 - answer of 20% of phoneprice
        print(discountPrice) #print the dicounted price of the phone

# create an instance object from the class MobilePhone blueprint/template
mobile1 = MobilePhone("OnePlus", "Black Slim Titanium", 10, 1203.31)
print(mobile1.make)
print(mobile1.description)
print(mobile1.model)
print(mobile1.price)



# print(make)
# create an instance object from the class MobilePhone blueprint/template
m2= MobilePhone("Samsung", "Folding phone", "Z-Fold", 1466.67)
print(m2.make)
# m3= MobilePhone()
# m4= MobilePhone()

#accessing method inside outer/main class
# need an instance object to access the method inside the outer/main class
m2.phoneDiscount()
# phoneDiscount()