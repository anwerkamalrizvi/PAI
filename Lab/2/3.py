Record = (("Affan", 40), ("Rahim", 68), ("Mustafa", 85),("Umer", 69), ("Ammar", 97))
swap = ( )
temp = list(Record)

for a in range(len(temp)):
    for b in range(len(temp) - 1):
        if(temp[b][1] < temp[b+1][1]):
            swap = temp[b]
            temp[b] = temp[b+1]
            temp[b+1] = swap
Record = tuple(temp)
print(Record)