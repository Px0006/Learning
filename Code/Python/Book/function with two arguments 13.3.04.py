list = []

def name(tame):
    input("What is your name: ")
    list.append(tame)

def streetName(stName, stNumber):
    stName = input("What is the name of your street? ")
    stNumber = input("And the street number? ")
    list.append(stName)
    list.append(stNumber)
    
def location(city, state, zipcode):
    city = input("What city do you live in? ")
    state = input("And what is the state or provice? ")
    zipcode = input("Finaly, what is the zipcode? ")
    list.append(city)
    list.append(state)
    list.append(zipcode)

def adress():
    name(1)
    streetName(1,1)
    location(1,1,1)
    print(list)

adress()



