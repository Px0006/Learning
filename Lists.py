numbers = [10, 5, 7, 2, 1 ]
numbers[0] = 111
numbers[1] = numbers[4]
print(numbers[0])
print(numbers)
print(len(numbers))
del numbers[1]
print(len(numbers))
print(numbers)
print(numbers[-1])
print(numbers[-2])
numbers.append(4)
print(len(numbers))
print(numbers)
numbers.insert(0,222)
print(len(numbers))
print(numbers)
numbers.insert(1,333)
print(numbers)

list = []
for i in range(5):
    list.insert(0, i + 1)
print(list)

list = [10,1,8,3,5]
sum = 0
for i in range(len(list)):
    sum += list[i]
print(sum)

list = [10,1,8,3,5]
sum = 0
for i in list:
    sum += i
print(sum)

list = [10,1,8,3,5]
list[0],list[4] = list[4],list[0]
list[1],list[3] = list[3],list[1]
print(list)

list = [10,1,8,3,5]
l = len(list)
for i in range(l//2):
    list[i],list[l - i - 1] = list[l - i - 1], list[1]
print(list)

list = [10,1,8,3,5]
print("List[-1]: ", list[-1])
print("list[-2]: ", list[-2])
l = len(list)
for i in range(l//2):
    list[i],list[l - i - 1] = list[l - i - 1], list[1]
print(list)

# Sample Solution

# step 1:
Beatles = []
print("Step 1:", Beatles)

# step 2:
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Step 2:", Beatles)

# step 3:
for members in range(2):
    Beatles.append(input("New band member: "))
print("Step 3:", Beatles)

# step 4:
del Beatles[-1]
del Beatles[-1]
print("Step 4:", Beatles)

# step 5:
Beatles.insert(0, "Ringo Starr")
print("Step 5:", Beatles)
print("The Fab:",len(Beatles))

#hat_list = [1, 2, 3, 4, 5]
#hat_list[2] = int(input("Enter a number: "))
#del hat_list [4]
#print(len(hat_list))
#print(hat_list)
