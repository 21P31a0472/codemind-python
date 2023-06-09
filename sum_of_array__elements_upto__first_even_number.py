n =int(input())
z = map(int,input().split())
k = 0
for i in z:
    if i % 2 != 0:
        k+=i
    elif i % 2 == 0:
        break
print(k)    
