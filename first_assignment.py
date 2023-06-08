s = input()  
count = 0  
result = []  

new = "" 
for char in s:
    new += char  

   
    if new.count('L') == new.count('R'):
        count += 1  
        result.append(new) 
        new = "" 

print(count) 
for char in result:
    print(char)