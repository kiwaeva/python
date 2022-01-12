class MobilePhone:
    def __init__(self,phoneMake, phoneDes, phoneModel, phonePrice ):
        #The self parameter is a reference to the current instance 
        # of the class, and is used to access variables that belongs to the class.
        #It does not have to be named self , you can call it whatever you like, 
        # but it has to be the first parameter of any function in the class:
        self.make =   phoneMake # "String Variable"
        self.description = phoneDes
        self.model = phoneModel
        self.price = phonePrice # 1234.7 = float data type
mobile1 = MobilePhone("OnePlus", "Black Slim Titanium", 10, 1203.31)
print(mobile1.make)
print(mobile1.description)
print(mobile1.model)
print(mobile1.price)


mobile2 = MobilePhone("Samsung", True, "Galaxy", 1103.31)
print(mobile2.make)
print(mobile2.description)
print(mobile2.model)
print(mobile2.price)

#Exercise 
#Create a third instance object from the class MobilePhone
#use different values from previous two objects instances
#print the values for the object instances you created

mobile3=MobilePhone("Meizu","Slim","17Pro", 670.79)
print(mobile3.make)
print(mobile3.description)
print(mobile3.model)
print(mobile3.price)
