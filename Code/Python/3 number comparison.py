# read two number
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

# we temporarily assume that the first number
# is the largest one
# we will verify it soon
max = number1

#check if the second value is larger than current max
# and update max if needed

if number2 > max: 
    max = number2

# we check if the third value is larger than current max
# and update max if needed
if number3 > max:
    max = number3

# print the result
print("The larger number is" ,max)
