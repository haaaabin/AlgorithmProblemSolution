str = input()
string =""

for s in str:
    if s.isupper():
        string += s.lower()
    else:
        string += s.upper()
        
print(string)