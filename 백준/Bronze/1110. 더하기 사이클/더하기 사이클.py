N = int(input())

result = N 
count=0 

while True:
    a = result //10  #십의 자리 
    b = result % 10  #일의 자리
    sum = a+b   #합        
    
    result = (b * 10) + (sum % 10) 
    count+=1
    if result == N:
        break
print(count)