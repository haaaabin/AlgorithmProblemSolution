alpha = 'abcdefghijklmnopqrstuvwxyz'
temp = input()

for i in alpha:
    if i in temp:
        print(temp.index(i), end = " ")
    else:
        print(-1, end = " ")