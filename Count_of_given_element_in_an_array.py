n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
for i in l:
    if i == k:
        s=s+1
print(s)