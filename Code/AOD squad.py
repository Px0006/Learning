AOD = [][:]
print("New AOD squad")

AOD.append("[Lieutentent] Mom")

for members in range(4):
    AOD.append(input("New squad members: "))

#del AOD[3] [remove private instruction]

#del AOD[0]  [remove lieutenent instuction]

#AOD.insert(0, "[lieutenent]") [insert lietentent instruction]

#AOD.append("private") [add private instruction]    

print("Squad size",len(AOD))
print(AOD)

AOD1 = AOD[:]
print(AOD1)
