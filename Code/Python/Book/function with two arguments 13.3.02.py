list = []

def Name(name):
    input("What is your name: ")

def streetName(stName):
    stName = input("What is the name of your street: ")
    list.append(stName)
    
def location(city, state, zipcode):
    city = input("What city do you live in: ")
    state = input("What reigon do you live in: ")
    zipcode = input("What country do you live in: ")
    list.append(city)
    list.append(state)
    list.append(zipcode)

location(1, 1, 1)

def printMyAdress(someName, houseNum):
    Name(1)
    print(houseNum)
    streetName(1)
    location(1,1,1)
    print("K2M 2E9")
    print(list)

printMyAdress("Carter Sandes","45")
printMyAdress("Jack Black","64")
printMyAdress("Tom Green","22")
printMyAdress("Todd White","36")


