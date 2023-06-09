n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    if l[i]%2!=0:
        k.append(l[i])
b=set(k)
print(len(b))