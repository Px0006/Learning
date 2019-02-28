row = []
#for i in range(8):
#    row.append(WHITE_PAWN)

#row = [WHITE_PAWN for i in range(8)]

squares = [ x ** 2 for x in range(10) ]
print(squares)

twos = [2 ** i for i in range(8)]
print(twos)

odds = [x for x in squares if x % 2 != 0]
print(odds)

#board = []
#for i in range(8):
#    row = [EMPTY for i in range(8)]
#    board.append(row)

temps = [[0.0 for h in range(24)] for d in range(31)]
print(temps)

#
# the matrix is magically updated here
#
sum = 0.0
for day in temps:
    sum += day[11]
average = sum/31
print("Average temp at noon: ", average)

max = -100.0

for day in temps:
    for temp in day:
        if temp > max:
            max = temp
print("The max temp was: ", max)

hotdays = 0

for day in temps:
    if day[11] > 20.0:
        hotdays += 1
print(hotdays, "days were hot")
