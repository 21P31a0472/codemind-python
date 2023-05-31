n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,len(l)):
    if i==l.count(i):
        c+=1
print(c)