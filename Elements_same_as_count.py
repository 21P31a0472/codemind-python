n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,len(l)):
    if l[i] == l.count(l[i]) and l[i] not in a:
        a.append(l[i])
if len(a)!=0:
    print(*a)
else:
    print("-1",end=" ")