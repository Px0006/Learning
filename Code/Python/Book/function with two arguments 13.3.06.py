list = []

def Address(name, stName, stNumber, city, state, zipcode):
    name = input("What is your name: ")
    stName = input("What is the name of your street? ")
    stNumber = input("And the street number? ")
    city = input("What city do you live in? ")
    state = input("And what is the state or provice? ")
    zipcode = input("Finaly, what is the zipcode? ")
    list.append(name)
    list.append(stNumber)
    list.append(stName)
    list.append(city)
    list.append(state)
    list.append(zipcode)
    print(list)

Address(1,1,1,1,1,1)
