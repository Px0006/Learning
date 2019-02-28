# creating a moving ball
class Ball:
    def __init__(self, color, size, direction,):  # initilization
        self.color = color  # attributes
        self.size = size
        self.direction = direction

    def __str__(self): # define string
        msg = "this is a " + self.size + " " + self.color + " ball"
        return msg

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall1 = Ball("red", "big", "down") # instance 1
myBall2 = Ball("green", "small", "down") # insance 2

print(myBall1)
print(myBall2)

print(myBall1.direction)
myBall1.bounce()
print(myBall1.direction)

print(myBall2.direction)
myBall2.bounce()
print(myBall2.direction)

# creating a simple ball class
#class Ball:
#    def __init__(self, color, size, direction):  # initilization
#        self.color = color  # attributes
#        self.size = size
#        self.direction = direction

#    def bounce(self):
#        if self.direction == "down":
#            self.direction = "up"

#myBall = Ball("red", "big", "down")  # instance
#print("I have a ball")
#print("it is ",myBall.size)
#print("as well as",myBall.color)
#print("and is headed",myBall.direction)
#print("lets bounce it")
#myBall.bounce() #bounce method
#print("now the ball is headed",myBall.direction) #direction method

#print(myBall.direction) #special function


# creating a simple ball class
#class ball:
#    def __init__(self, color, size, direction): #initilization
#        self.color = color
#        self.size = size
#        self.direction = direction

#    def bounce(self):
#        if self.direction == "down":
#             self.direction = "up"
             
#             myBall = ball() #instance

              #attributes
#             myBall.direction = "down" #object direction
#             myBall.color = "green"
#             myBall.size = "small" 
#             myBall.bounce() #bounce method
#             myBall.direction #direction method
             
#print(myBall)

#def foo1(val1, val2, val3):
#	return val1 + val2 + val3

#def foo2(val4):
#    print("Hello from  within foo")
#    return val4

#def bar():
#return 

#if foo1() >= foo2():
#    print("5")
#else:
#    foo1 <= foo2
