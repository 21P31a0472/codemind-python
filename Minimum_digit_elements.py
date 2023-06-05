n=int(input())
m = list(map(int,input().split()))
k=[]
for i in m:
    k.append(len(str(i)))
b=min(k)
c=0
for i in k:
    if i==b:
        c=c+1
print(c)