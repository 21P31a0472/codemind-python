r,c=map(int,input().split())
se=0
so=0
for i in range(r):
    if i%2==0:
        l=list(map(int,input().split()))
        se=se+sum(l)
    if i%2!=0:
        l=list(map(int,input().split()))
        so=so+sum(l)
print(se,so)