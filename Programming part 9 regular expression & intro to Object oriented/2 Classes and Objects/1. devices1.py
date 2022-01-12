# To understand the meaning of classes we
# have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is
#  always executed when the class is being initiated.
#  Use the __init__() function to assign values to object
#  properties, or other operations that are necessary to do
#  when the object is being created:

# Object Oriented programming: object have three things
#  Identity/Name, Properties/Variables, Functionality/Behaviour.
# Objects communicates with each other through Functionality and Behaviours,
# and exchange data via properties or variables
""" The init built in Python method available for every class and takes the
 keyword self"""
""" Self points to the current object been created of this particular class """
""" Use the init method to define and assign values to fields """

#Class is a blueprint/template
class MobilePhone: # define a class name with upper case
    #  Use the __init__() function to assign values to object (constructs an object of the class)
    def __init__(self):
        self.make = "Samsung"  #name is Property/Variable and "Samgung" is the value held in variable name
        self.description = "Slim Buid, touch screen"
        self.model = "Galaxy S10"
        self.price = 945

mobile1 = MobilePhone()  # create an object instance (mobile1) from the class MobilePhone
print(mobile1.make) #use instance object mobile1 to access class variable and value
print(mobile1.description) #use instance object mobile1 to access class variable and value
print(mobile1.model)
print(mobile1.price)

mobile2 = MobilePhone()  # create an object instance (mobile1) from the class MobilePhone
mobile2.description = "Touchscreen and foldable" #modify/reset the value of the variable specified in the class
mobile2.model = "Z-Fold"
mobile2.price = 1235

print("\nSecond instance object of Mobile phone")
print(mobile2.make )  #use instance object mobile1 to access class variable and value
print(mobile2.description)
print(mobile2.model)
print(mobile2.price)

mobile3 = MobilePhone()
mobile3.make = "iPhone"
mobile3.description = "Touchscreen Pixel"
mobile3.model = "11"
mobile3.price = 1635

print("\nThird instance object of Mobile phone")
print(mobile3.make )  #use instance object mobile1 to access class variable and value
print(mobile3.description)
print(mobile3.model)
print(mobile3.price)
