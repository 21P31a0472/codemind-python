n=int(input())
l=list(map(int,input().split()))
a=sum(l)//len(l)
c=0
for i in l:
    if i>=a:
        c=c+1
print(c)