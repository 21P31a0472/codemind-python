n=int(input())
l=list(map(int,input().split()))
c=0
av=sum(l)//n
for i in l:
    if i<=av:
        c=c+1
print(c)

    