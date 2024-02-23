import sys
input = sys.stdin.readline

n = int(input())
temp = {}
for i in range(n):
    name,log = map(str,input().split())
    temp[name] = log
    if log == "leave":
        del temp[name]
    
tp = sorted(temp.items(), reverse = True)
dic = dict(tp)

for key in dic.keys():
    print(key)