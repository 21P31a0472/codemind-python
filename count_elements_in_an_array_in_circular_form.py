n=int(input())
l=list(map(int,input().split()))
t=[]
c=0
t.append(l[-1])
for i in l:
    t.append(i)
t.append(l[0])
for i in range(1,n+1):
    if ((t[i-1] % 2 == 0 and t[i+1] % 2 != 0 ) or (t[i-1] % 2 != 0 and t[i+1] % 2 == 0)):
        c=c+1
print(c)