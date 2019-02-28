list = []

def Address(name, stName, stNumber, city, state, zipcode):
    name = input("Hi, I am Px <|-_-|>\n What is your name: ")
    stName = input("What is the name of your street? ")
    stNumber = input("And the street number? ")
    city = input("What city do you live in? ")
    state = input("And what is the state or provice? ")
    ziporPost = input("Finaly, what is your zip or postal code? ")
    list.append(name)
    list.append(stNumber)
    list.append(stName)
    list.append(city)
    list.append(state)
    list.append(zipcode)

Address(1,1,1,1,1,1)

print("Thank you for your time <|-_-|>")
