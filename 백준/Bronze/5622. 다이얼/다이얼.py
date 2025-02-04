dict = {'ABC' : 3,
        'DEF' : 4,
        'GHI' : 5,
        'JKL' : 6,
        'MNO' : 7,
        'PQRS' : 8,
        'TUV' : 9,
        'WXYZ' : 10
        }

alpha = input()
result = 0

for i in alpha:
    for key, value in dict.items():
        if i in key:
            result += value

print(result)