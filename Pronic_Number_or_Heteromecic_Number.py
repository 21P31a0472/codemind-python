n=int(input())
k=0
for i in range(0,n+1):
    if i*(i+1) == n:
        print("YES")
        k = 1
        break
if k == 0:
    print("NO")