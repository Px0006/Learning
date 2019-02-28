max = -99999999999
counter = 0

while True:
    number = int(input("Enter a value: "))
    if number ==-1:
        break
    counter += 1
    if number > max:\
       max = number
if counter:
    print("The largest number is" ,max)
else:
    print("Are you kidding? You haven't entered any value!")

i = 5
while 1 < 5:
    print(i)
    i += 1
else:
    print("else:",i)
