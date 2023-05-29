n = int(input())
l = list(map(int,input().split()))
m=0
k=[]
for i in range(n):
    if i % 2 != 0:
        k.append(i)
for i in k:
    if l[i] % 2 != 0:
        m=m+1
if m == len(k):
    print("True")
else:
    print("False")