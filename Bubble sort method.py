list = [8,10,6,2,4] #list to sort
swapped = True # it's a little fake - we need it to enter the while loop
#we need (5-1) comparisons
while swapped:
    swapped = False # no swaps so far
    for i in range(len(list) - 1):
               if list[i] > list[i + 1]:
                          swapped = True # swap occured!
                          list[i],list[i + 1]=list[i + 1],list[i]


print(list)

# Interactive bubble sort

list = []
swapped = True
num = int(input("How objects many objects would you like to put in the container: "))
for i in range(num):
    val = int(input("Please enter the integer value of the object: "))
    list.append(val)
while swapped:
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i],list[i + 1]=list[i + 1],list[i]
print("sorted:")
print(list)

first_list = [5, 8, 1, 0, 100, 4, 7, 22, 6]
#first_list.sort()  # object sort method
print(first_list)

first_list.insert(0, 48)
print(first_list)

first_list.insert(1, 23)
print(first_list)

first_list.insert(-11, 77)
print(first_list)


