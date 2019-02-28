class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "raw"
        self.condiment = []

    def __str__(self):
        msg = "hot dog"
        if len(self.condiment) > 0:
            msg = msg + " with"
        for i in self.condiment:
            msg = msg+i+", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg

    def cook(self, time):
        if self.cooked_level > 8:
            self.cooked_string = "charcol"
        elif self.cooked_level > 5:
            self.cooked_string = "well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "medium"
        else:
            self.cooked_string = "raw"

    def addCondiment(self, condiment):
        self.condiment.append(condiment)

myDog = HotDog()
print(myDog)
print("Cooking hotdog for 4 minutes")
myDog.cook(4)
print(myDog)
print("Cooking hotdog for 3 more minutes")
myDog.cook(3)
print(myDog)
print("What happens if you cook it for 10 more minutes")
myDog.cook(10)
print(myDog)
print("Now, I'm going to add some stuff on my hotdog")
myDog.addCondiment(" ketchup")
myDog.addCondiment("mustard")
print(myDog)