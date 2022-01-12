class MobilePhone: #outer class
    def __init__(self,phoneMake, phoneDes, phoneModel, phonePrice ):
        self.make =   phoneMake # "String Variable"
        self.description = phoneDes
        self.model = phoneModel
        self.price = phonePrice # 1234.7 = float data type
    
    class IMEInumber: # inner class
        def __init__(self, imeiNo,fSize):
            self.number = imeiNo
            self.fontSize= fSize
    class ScreenSize:
        def __init__(self,sSize):
            self.size=sSize


#exercise add and then access the third paramter in the innerClass IMEInumber

# create another inner class an called it, screenSize with only one parameter 
# print the value of the screensize paramter
m3= MobilePhone("OnePlus", "Black Slim Titanium", 10, 1203.31)

phoneScreenSize=m3.ScreenSize("ScreenSize is ...")

print(phoneScreenSize.size)
####
mobile1 = MobilePhone("OnePlus", "Black Slim Titanium", 10, 1203.31)
phoneScreenSize=mobile1.ScreenSize("blblkbkblb")
print(phoneScreenSize.size)

####
mobile1 = MobilePhone("OnePlus", "Black Slim Titanium", 10, 1203.31)
print(mobile1.make)
print(mobile1.description)
print(mobile1.model)
print(mobile1.price)


#access inner class
#creat an instance object to access the inner class
m2= MobilePhone("HTC","Outdated","Unavailable",156.22)

phoneImeiNo=m2.IMEInumber(34567890, "Size12")

print(phoneImeiNo.number)
print(phoneImeiNo.fontSize)

# IMEInumber()
