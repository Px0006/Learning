list1 = [1]
list2 = list1
list1[0] = 2
print(list2)

list3 = [10,8,6,4,2]
new_list = list3[:3]
new_list = list3[0:]
print(new_list)

# del list3
print(list3)

list4 = [0, 3, 12, 8, 2]
print(5 in list4)
print(5 not in list4)
print(12 in list4)

