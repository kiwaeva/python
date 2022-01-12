import re

varString = "I am learning to program python, with practice I will be good in python programming"

search=re.findall(r'python',varString)
print(search)

search=re.findall(r'p\w+',varString)
print(search)

search=re.findall(r'p\w*',varString)
print(search)

search=re.findall(r'p\w?',varString)
print(search)

search=(re.split(r"\s",varString))
print(search)

search=len(re.split(r"\s",varString))
print(search)

search=re.sub(r'good','proficient',varString)
print(search)

#####my solution


# class MobilePhone:
#     def __init__(self):
#         self.make = (input("Enter phone name: "))
#         self.description=(input("Enter description: "))
#         self.model =(input("Enter a model: "))
#         self.price=(int(input("Enter price: ")))

# mobile1=MobilePhone()
# print(mobile1.make)
# print(mobile1.description)
# print(mobile1.model)
# print(mobile1.price)



####right solution
class MobilePhone:
    def __init__(self):
        self.make = "Samsung"
        self.description="Slim Build, touch screen"
        self.model ="Galaxy S10"
        self.price=945

mobile1=MobilePhone()
mobile1.make=input("Enter phone name: ")
mobile1.description=input("Enter description: ")
mobile1.model=input("Enter a model: ")
mobile1.price= float(input("Enter price: "))


print("Mobile make is: ",mobile1.make)
print("Mobile description: ",mobile1.description)
print("Mobile model is: ",mobile1.model)
print("Mobile price is: £",mobile1.price)
