def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])

try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")



try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

try:
  print(1)
except:
  print(2)
finally:
  print(3)
  
#try:
#  print(1 / 0)
#except ZeroDivisionError:
#  raise ValueError

print(0)

print (1)
#assert False
print(2)
#assert True
print(3)

name = 'initVal'
#output
#message: text to write user
#output algorithm
#output the text message
#output code -- output the text message
print('message')
#input
#variable: where answer from user will be stored
#message: question being asked of the user
#input algorithm
#ask the user message and tore the anser in variable
variable = input('message')
#convert to interger code
#covert oldVariable to integer and store in intVariable
intVariable = int(4)

def stuf(a,b):
    return a + b

stuf(1,1)


def stuff(a,b):
  a = 0
  b = 0
  a = int(input('enter a number: '))
  b = int(input('enter a number: '))
  return a + b

print(stuff(1,1))


#create an integer variable for x
x = 0
#create an intger variable for y
y = 0
#create an inter variable for sum
#sum(x+y)

#ask th user "x: " and put answer in x
x = input("X: ")
#ask th user "x: " and put answer in y
y = input("Y: ")

#convert x to integer
#x = int(x)
#convert y to integer
#y = int(y)

#put x + y in sum
#Ssum(x+y)

#tell user "answer is" sum
print("sum is ")

file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()


#backend calls
#connect to a database
#bring in some users
#get neighbor
#hash table
#arrary
#tree traversals
#connected group of nodes
#array if integers
#iterate
#search function
#call each neighbor
#is valied get neighbors
#array of cordinates binary
#duplicate detection
#colision
#time space
#recursive algorithm
#stack overflow
#stack space#
#10000 itteration#
#grid size
#iteratize solution
#memory size
#stack que
#push neighbor
#time space analysis
#recuresive or iterative in linear time hash table in constant time recursive
#algorithm simpler to read iterative a little more comeplex,
#but not limited on stack space
#matrix(n) and visit n items, that is your run time
#client with back
#communication with backend through api
#how did you define the api
#communication mechanism
#json xml
#how did the client get the data back
#how did you use the data
#what language originated on
#technical challanges
#analysys
#talk through and analyse th solution
#time space analysis
#basic python control flow
#if,else, for, while loops
#display cpu or ram
#web scraper
#interview problems
#fiz buz
#fibonachi
# data types
#list, tuples, dict, set
#Variable Declaration
#


def stuf(a,b):
    return a + b

stuf(1,1)

#Roll the Ball (Animated)

given_array = [1,4,3,2 ..., 10]

def find_sum(given_array):
  total = 0 #initialize a variable
  for each i in given_array:
      total += 1
  return total #sum of all numbers in the array
#How much time to run this function?
#How does the runtime of this function grow?
#runtime = time it takes to execute a piece of code
#Big O Notation and Time Complexity
#feb 28, 2019 Px0006
#
