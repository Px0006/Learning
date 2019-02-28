list = []

def location(city, region, country):
    city = input("What city do you live in: ")
    region = input("What reigon do you live in: ")
    country = input("What country do you live in: ")
    list.append(city)
    list.append(region)
    list.append(country)
    print(list)

location(3, 4, 1)

def printMyAdress(someName, houseNum):
    print(someName)
    print(houseNum)
    print("Main Street")
    location(3,4,1)
    print("K2M 2E9")
    print()

printMyAdress("Carter Sandes","45")
printMyAdress("Jack Black","64")
printMyAdress("Tom Green","22")
printMyAdress("Todd White","36")


