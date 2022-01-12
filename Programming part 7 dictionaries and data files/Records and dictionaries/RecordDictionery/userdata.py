
#declare a dict var with only keys
userData={"Fullname": "","Course":"","Module":""}

userData["Fullname"]=input("Enter your full name: ")
userData["Course"]=input("Enter your course name: ")
userData["Module"]=input("Enter your module name: ")

print(userData)


#Task Create a record
#Use the dictionary data structure to create a record for a film
# Your record should have at least three attributes. 
# Movie title, Actor(s), Realease Date
#Test your dictionary by printing it.

filmData={"MovieName":"", "Actors":"","ReleaseDate":""}

filmData["MovieName"] = input("Enter the name of the movie: ")
filmData["Actors"] = input("Enter the lead actor of the movie: ")
filmData["ReleaseDate"] = input("Enter the year of release: ")

print(filmData)