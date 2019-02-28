while conditional_expression
    instruction_1
    instruction_2
    instruction_3
    :
    :
    instruction_1

while True:
    print("I'm stuck in a loop")

max = -9999999999999

number = int(input("Enter value or -1 to stop"))

while number != -1:

    if number > max:

        max = number

    number = int(input("Enter value or -1 to stop: "))

print("the Largest number is" ,max)

# program reads a reads a seqence of numbers and counts how many numbers
# even and how many are odd
# program terminates when zero is entered

Even = 0
Odds = 0
#read first number
Number = int(input("Enter a value or 0 stop: "))
# 0 terminates execution
while Number !=0:
    # check if the number is odd
    if Number % 2 == 1:
        # increase "odd" counter
        Odds += 1
    else:
        # increase "even" counter
        Even += 1
    #read next number
    Number = int(input("Enter a value or 0 to stop: "))
# print results
print("Even number: " ,Evens)
print("Odd numbers: " ,Odds)

while number != 0:
while number:

if Number % 2 == 1:
if Number % 2:

counter = 5;
while counter != 0:
    print("My name is Python...")
    counter-= 1

counter = 5;
while counter:
    print("My name is Python...")
    counter-= 1

i= 0
while i < 100:
    # do something
    i += 1

for i in range(10):
    print("Value of i is currently" ,i)
