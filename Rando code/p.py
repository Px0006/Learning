n = 5
m = 1
for i in range(0,n):
    for j in range(0,i+1):
        m=i+j+1
        print((m),end='')
    print("\r")

#i

def sequenceMax(self,l1):
    self.l1 = l1
    l1 = [int(x) for x in l1]
    l1 = int
    self = int
    split = int
    counter = 1
    for i in range(len(l1)):
        if l1[i] == l1[i+1]:
            counter += 1
        else:
            counter = 1  
    return counter

numbers=input("Enter a list of values separated by commas: ")
sequenceMax(1,1)
