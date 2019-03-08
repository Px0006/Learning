# Python example code
# I am trying to make a massive example script, demonstrating all of the core syntax of Python (beginner to intermediate and maybe advanced).
# It could serve as a tutorial even. 

# I want it to be one sample project that includes all of the following syntax for python, but I can't think of a good example. Could use some help.
# I also want to do the same thing for LUA and eventually C#. I would like to use the same example.
# I used the analogy of cooking to make an intro to computer programming course, so I guess I could go with that, but I don't exactly know
# how I would incorporate all of the following constructs. 

# I could do the whole boring data base thing, but it's boring. 

 

Currently the examples are unrelated. 

 

Here is what I have so far:

# -*- coding: utf-8 -*-
print "Python Examples\n --By The Tutorial Doctor\n"

## PRINTING

print 'Hello'

print 'Hello','Editorial'

# Concatenate/Append text (gives errors if not strings)
print 'Hello' + 'Folks'

print 'Hello' + ' Folks' # have to add your own space

print 27


# VARIABLES
#There are different types of variables: character, string, integer, float, boolean, array/list, dictionary, and a few others.

# A character
at = "@"

# A string
name = 'Jackie'

# An integer
favorite_number = 4

# A float
height = 6.5

# A boolean
IamCool = True 

# You can assign a new value to a variable
IamCool = False 

# An array
array_of_colors = ['red','orange','yellow','green','blue','indigo','violet']
array_of_numbers = [23,13.4,1,782]
mixed_array = ['Zillow',34.9,True,798]

# A dictionary
description = {'eyeColor':'brown','physique':'muscled','demeanor':'confident'}
print description['eyeColor']
print description['physique']
print description['demeanor']

# EXTRA

# ID of a variable
print id(name)

#####

# STRINGS
# A string is string of characters 

## Empty string
first_name = ""
last_name = ""


## Asign a value to a string
first_name = "joe"
last_name = "shmo"
occupation = "Truck Driver"


## Adding strings (concatenation)
print first_name + last_name

## Adding a space between string variables
print first_name + " " + last_name

## Starting a new line (escape characters)
print first_name + "\n" + last_name 

## Adding variables inside of a string (string formatting)
print "Hello %s" %(first_name)

## Multiple variables inside of a string
print "Hello %s %s" %(first_name,last_name)

## There is another way to format strings
greeting = 'Hello {name}, my name is {myname}'
print greeting.format(name='Joseph',myname='Joey')

## Print a string several times
print first_name * 4

## Get index of a string
## Indices begin at 0
print first_name[0]
print first_name[1]
print first_name[2]

## A multi-line string
"""Multi-Line strings are sometimes used as multi-line comments, since python doesn't have syntax for multi-line comments."""


# STRING FUNCTIONS
print first_name.capitalize()
print len(occupation) 

#####

# INTEGERS
# An integer is a whole number

number1 = 12
number2 = 144
number3 = "67" #not an integer

#Add
print number1 + number2

#Subtract
print number2 - number1

#Multiply
print number1 * number2

#Divide
print number2/number1

#Exponents
print number2**number1
#Same
print pow(number2,number1)

#Square root
print number2**(1/2.0)

#Order of operations
print (number1 + number2) * 3 + (number1**3)

# Increment an integer
number1 = number1 + 1
print number1

# Convert a string to an integer
number3 = int(number3)

#####

#FLOAT
# A float is a decimal. Many of the integer operations can be applied to floats.
pi = 3.14
print pi
#####

# TUPLES
## Tuples are like lists, but cannot be changed (they are immutable).

x = 0
y = 1


## Create a Tuple
position = (50,200)


## Get tuple index
print position[x]

#####

# LISTS/Array
# Called a list in python.

# Create a list
Clients = ['Cierra','Lisa','Ibrahim','Eric','Nancy','Terry','Sarah']
print Clients

Employees = ['Eric','Margaret','Paul','Ole','Yul']
print Employees

### LIST FUNCTIONS
# List Index
print Clients[0]

# List index range
print Clients[0:4]

# Append to a list
Clients.append('Joe')
print Clients
#Same as:
#Clients[len(Clients):] = ['Joe'].

# Remove from a list
Clients.remove('Joe')
print Clients

# Insert item into a list at a location
Clients.insert(0,'Lee')
print Clients

# Reverse a list
Clients.reverse()
print Clients

# Sort a list
Clients.sort()
print Clients

# Remove an item at a location
Clients.pop(0)
print Clients

# Return the index of an item in the list
print Clients.index('Lee# Extend a list with another list
Clients.extend(Employees)
print Clients
# Same as:
#Clients[len(Clients):] = Clients

# Count how many times an item appears in a list
print Clients.count('Lisa
### EXTRA

# Loop through a list
for item in Clients:
	print item
	
#Remove a list from a list
for i in Clients:
		if i in Employees:
			Clients.remove(i)
print Clients

#####

### DICTIONARIES/Associative array

# Create a dictionary (dictionary_name = {key:value})
inventory = {'light':'flashlight'}
print inventory


# Print the value of a key
print inventory['light']


# Update Dictionary 
inventory.update({'map':'New York'})
inventory.update({'phone':'Flip Phone'})
print inventory


# Update the key if it is already in the dictionary
inventory.update({'map':'Atlanta'})
inventory.update({'map':'New York'})
print inventory['map']


# Get all keys (outputs as a list)
print inventory.keys()


# Get all values (ouptuts as a list)
print inventory.values()


# Copy dictionary items as a list of tuples
# Basically converts a dictionary to a a list of tuples.  
print inventory.items()


# Length of a dictionary
print len(inventory)


# Delete inventory item
del inventory['map']
print inventory


# Iterate over dictionary
#print iter(inventory)
#print inventory.iterkeys()
#print inventory.itervalues()

# Remove item, and returns its value
inventory.pop('phone Alternately: inventory.popitem()
print inventory

# View keys of a dictionary
print inventory.viewkeys()

# View values of a dictionary
print inventory.viewvalues()

# View all items in a dictionary
print inventory.viewitems()

#####

### CONDITIONALS

on = True
number = 51

# If equal to
if on == True:
	print on

# Same (for booleans)
if on:
	print on

# If not equal to
if on != False:
	print on

# If greater than
if number > 23:
	print number

# If less than
if number < 77:
	print number

#####

## BOOLEANS (BEG)
# if, else, and else if(elif)

location = 0
	
if location == 50:
	print 'Halfway there.'
elif location > 50 and location < 100:
	print 'More than halfway there.'
elif location < 50 and location > 0:
	print 'Less than halfway there.'
elif location == 100:
	print "You are there!"
elif location < 0:
	print "You're moving in the wrong direction!"
elif location > 100:
	print "You've gone too far."
elif location ==  0:
	print "You aren't moving!"

#####

### WHILE LOOP
age = 0
old_age = 30

while age < old_age:
	print 'Still young @ ' + str(age)
	age = age + 1
if age ==  old_age:
	print "You've reached the pinnacle @ " + str(age)
	
#####

### FUNCTIONS
# A function is a group of statements

IamCool = True
### BUILT-IN FUNCTIONS
# print() - Prints values to the screen
print(name)
print(favorite_number)

# Two ways to print
print height
print IamCool,",I am cool"

print array_of_colors
print array_of_numbers


# raw_input() - Gets input from the user
occupation = raw_input('What is your occupation? ')
print 'You are a ' + occupation

# len() - Gets the length of a string
print(len(name))

# type() - Gets the type of a value
print(type(height))

# str() - Converts a value to a string
print(type(str(height)))

# int() - Converts a value to an integer
print(type(int(height)))

# list() - Converts a value to a list

# float() - Converts a value to a float

# round() - Rounds a number to a given percision
print(round(height,2))
print(round(height,1))


# pow() - Raises a number or integer to a power 
power = pow(height,favorite_number)
print(power)

# sum()- sum of all elements in an iterable 
print 'sum of array is',sum(array_of_numbers)

# help() - prints Python help information
#help() commented out for now


# Create a function
def MyFunction():
	print name
	print height
	print favorite_number

# Use/Call a function
MyFunction()

## Function arguments
# One argument
def Write(first_name):
	print first_name
	
Write('Ole')

# More than one argument (separated by commas)
def Add(a,b):
	print 'The sum is ' +  str(a + b)

Add(2,3)
Add(2.89,34.2)

# Function return
def Multiply(a,b):
	product = a*b
	return product

print 'The product is',Multiply(2,89)

#####

### FOR LOOP

print range(0,10)

# Loop over a range
for i in range(0,10):
	print i
# For each element inside of the range, print the element.

# Loop over a string
name = 'Joseph'
for letter in name:
	print letter

# Loop over a list
my_list = ['eggs','milk','bread']
for item in my_list: 
	print item

#####

# WHILE LOOP
i = 1
while i<11:
	print "uh",i, "and"
	i = i + 1 #increment i

### CLASSES

# A class
class Fruit():
	def __init__(self,color,taste,type='Fruit'):
		
		# Member Variables
		self.color = color
		self.taste = taste
		self.type = type
	
	# A Method	
	def eat(self, item):
		print "Eating " + item

# An object
apple = Fruit("red","sweet")

# Accessing member variables
print(apple.color)
print(apple.taste)
print(apple.type) # default value. a non-required argument.

# Using methods
apple.eat("vegetables####

# Try to do something, and if there is an error, do something else
try:
    print "Hello World"
except:
	print('Goodbye World')

# Types of exceptions
exceptions= """except IOError:
    print('An error occured trying to read the file.')
    
except ValueError:
    print('Non-numeric data found in the file.')

except ImportError:
    print "NO module found"
    
except EOFError:
    print('Why did you do an EOF on me?')

except KeyboardInterrupt:
    print('You cancelled the operation.')

except:
    print('An error occured.')
"""

#####

### PART 2 ###

# -*- coding: utf-8 -*-
# BOOLEANS

cold = False
hot = False
normal = False

cloudy = False
partly_cloudy = False
sunny = False


temp = 12
overcast = 68


if temp < 65:
	cold = True
	

if temp > 85:
	hot = True


if temp > 65 and temp < 85:
	normal = True

	
if overcast > 55:
	cloudy = True


if overcast < 30:
	sunny = True

	
if overcast > 30 and overcast < 55:
	partly_cloudy = True
	
	
if (cold and cloudy) and (cold and partly_cloudy):
	print 'Its gonna be a yucky day'
else:
	print 'Its an okay day out!'
	
	
if (cold and cloudy) or (cold and partly_cloudy):
	print 'Its gonna be a yucky day'
else:
	print 'Its an okay day out!'
	
	
if hot and sunny:
	print 'Its gonna be steaming!!'

class Animal():
	# two underscores mean the variable is private
	__name = ""
	__height = 0
	__weight = 0
	__sound = ''
	def __init__(self,name):
		self.__name = name
		
	def get_name(self):
		print self.__name

a = Animal('a')

a.get_name()

# CONDITIONALS

adult = False
miniumum_age = 18

def CheckAge():
	age = int(raw_input('How old are you: '))
	if age >= miniumum_age:
		adult = True
		print 'You are legal'
	elif age < miniumum_age:
		print 'That is not old enough'
		adult = False
	
	if not adult:
		CheckAge()
CheckAge()

# FUNCTIONS (INTERMEDIATE)
welcome = 'Welcome to Editorial! '
response = raw_input('How are you today? ')
computer_response = 'It seems you are ' + response

# Create a function
def PrintSomething():
	print 'Hi'
	
# Call the function
PrintSomething()

# Function arguments/parameters
def PrintArgument(argument):
	print argument

PrintArgument(welcome)
PrintArgument(computer_response)

def push_argument(*argparams):
	print argparams
push_argument('a','b')


def push_keys(**keyparams):
	print keyparams
push_keys(ok='right')


def default_parameters(a='A',b='B'):
	print a,b
default_parameters(a='Not A',b='Not B')


def fixed_passed_parameters(a,b):
	print a,b
fixed_passed_parameters('a','b')


#String Funtions
import string

name = 'john jacob jingleheimer schmidt'

place = 'Wasington D.C.'
print place

place = place.lower()
print place

place = place.upper()
print place

## FOMATTING
formatted_string ='My name is %s' % ('Mr Editorial')
print formatted_string

multiVariable_formatted_string = "He crossed the %(blank)s at %(time)d o'clock" % {'blank':'street','time':12}
print multiVariable_formatted_string


## CLASSES
place = string.capitalize(place)
print place

split_name = string.split(name,None,-1)
print split_name

joined_split_name = string.join(split_name)
print joined_split_name

print string.capwords(joined_split_name,None)

# -*- coding: utf-8 -*-

# BETTER WAY

temperature = -10

initial_position = 0
final_destination = 100
halfway_point = (final_destination-initial_position)/2
location = ''
	
while temperature < final_destination:
	diff = final_destination-temperature
	temperature = temperature + 1
	if temperature == halfway_point:
		location= 'Halfway there.'
		print str(temperature) + ' is ' + location + str(diff) + ' More to go!'
	elif temperature > halfway_point and temperature < final_destination:
		location= 'More than halfway there.'
		print str(temperature) + ' is ' + location + str(diff) + ' More to go!'
	elif temperature < halfway_point and temperature > initial_position:
		location= 'Less than halfway there.'
		print str(temperature) + ' is ' + location + str(diff) + ' More to go!'
	elif temperature == final_destination:
		location= "There!"
		print str(temperature) + ' is ' + location + ' No more to go!'
	elif temperature < initial_position:
		location= "Negative!"
		print str(temperature) + ' is ' + location + str(diff) + ' More to go!'
	elif temperature > final_destination:
		location= "Too far."
		print str(temperature) + ' is ' + location + str(diff) + ' More to go!'
	if temperature >= (temperature-1):
		print 'going in the right direction'
	else:
		print 'Wrong way Josè!'

