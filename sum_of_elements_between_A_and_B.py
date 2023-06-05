n=int(input())
l =  list(map(int,input().split()))
a,b = map(int,input().split())
k =0
for i in l:
    if i<=b and i>=a:
        k=k+i
print(k)