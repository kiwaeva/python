

class Car:
    def __init__(self,make,year):
       self.carMake= make
       self.carYear= year
    
    def startCar(self):
        print("Start car")

    class Engine:
        def __init__(self,engNo):
            self.engineNumber = engNo

class BMW(Car):#create a sub class and pass the name of the superClas inside the brackets
    def __init__(self, cruisedControl,make, year):
        #invoke the parent class constructor #def __init__
        super().__init__(make, year)
        #variable cc belongs only to the subclass class BMW
        self.cc = cruisedControl
class Tesla(Car):
    def __init__(self,entSys, make, year):
        super().__init__(make, year)
        self.eSystem= entSys

subCar2 = Tesla("mp3/4 player navigation","Tesla","2020")
print(subCar2.eSystem)
print(subCar2.carMake)
print(subCar2.carYear)


subCar = BMW("Enabled","BMW", 2021)
print(subCar.cc)
print(subCar.carMake)
print(subCar.carYear)

# car1= Car ('Tesla',2020)

# print(car1.carMake)
# print(car1.carYear)
# #Call/invoke the method start car
# car1.startCar()
# #create an object of the outer class to create an object of the inner class
# e = car1.Engine(12345)
# print(e.engineNumber)


