keys = []
for i in range(9):
    keys.append(int(input()))

keys.sort()     #정렬

temp1 = 0
temp2 = 0
for i in range(9):
    for j in range(i+1,9):
        if sum(keys) - (keys[i]+ keys[j]) == 100:
            temp1 = keys[i]
            temp2 = keys[j]
            
keys.remove(temp1)
keys.remove(temp2)

for key in keys:
    print(key)