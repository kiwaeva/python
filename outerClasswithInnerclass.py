class MobilePhone: #outer class
    def __init__(self,phoneMake, phoneDes, phoneModel, phonePrice ):
        self.make =   phoneMake # "String Variable"
        self.description = phoneDes
        self.model = phoneModel
        self.price = phonePrice # 1234.7 = float data type
    
    class IMEInumber: # inner class
        def __init__(self, imeiNo):
            self.number = imeiNo

mobile1 = MobilePhone("OnePlus", "Black Slim Titanium", 10, 1203.31)
print(mobile1.make)
print(mobile1.description)
print(mobile1.model)
print(mobile1.price)