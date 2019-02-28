# read two number
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# choose the larger number
if number1 > number2:
    max = number1
else:
    max = number2

# print the result
print("The larger number is" ,max)

word = input("word of the day: ")
if word == "spathiphyllum": print("Spathiphyllum is the best plant ever!")
else: print("No, I want a real Spathiphyllum...!")
