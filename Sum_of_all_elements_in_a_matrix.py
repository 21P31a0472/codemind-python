r,c=map(int,input().split())
se=0
for i in range(r):
        l=list(map(int,input().split()))
        se=se+sum(l)
print(se)