class MobilePhone: #outer class
    def __init__(self,phoneMake, phoneDes, phoneModel, phonePrice ):
        #The self parameter is a reference to the current instance 
        # of the class, and is used to access variables that belongs to the class.
        #It does not have to be named self , you can call it whatever you like, 
        # but it has to be the first parameter of any function in the class:
        self.make =   phoneMake # "String Variable"
        self.description = phoneDes
        self.model = phoneModel
        self.price = phonePrice # 1234.7 = float data type

    #create function in a class
    def phoneDiscount(self): # method inside the outer class ony
        calcDiscount = self.price * 0.2
        discountPrice = self.price - calcDiscount
        print(discountPrice)
    
    #create an inner class
    class IMEInumber: # inner class
        def __init__(self, imeiNo):
            self.number = imeiNo
        
        #create function/method inside the inner class
        def checkImei(self):
            print("valid")

#exercise access the method checkImei inside the inner class IMEInumber

#first instance object of mobile phone class
mobile1 = MobilePhone("OnePlus", "Black Slim Titanium", 10, 1203.31)
print(mobile1.make)
print(mobile1.description)
print(mobile1.model)
print(mobile1.price)


# access the method via the instance object created 
# from the class using the dot notation
mobile1.phoneDiscount()

# access the inner class via the instance object created 
# from the class using the dot notation via the outer class
phoneImeiNo = mobile1.IMEInumber(1234567890)

print(phoneImeiNo.number)

#answer to exercise
print("\n Your IMEI number is: ")
phoneImeiNo.checkImei()

#                  1st level   inside 1st level
#variable        outer class   inner method
"classFunction = MobilePhone().phoneDiscount()"

#               1st level   second level inside 1st level
# variable    outerclass    innerclass
"innerClass = MobilePhone().IMEInumber()"

#                           1st level   second level    inside second level
#variable                  outer class   inner class inner method
"innerMethodinInnerClass = MobilePhone().IMEInumber().checkImei()"


# m2 = MobilePhone()
# m2.phoneDiscount()

# def phoneDiscount(self):
#     calcDiscount = self.price * 0.2
#     discountPrice = self.price - calcDiscount
#     print(discountPrice)