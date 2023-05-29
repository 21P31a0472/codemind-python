z=int(input())
l=list(map(int,input().split()))
m=0
x=[]
for i in range(z):
    if i%2==0:
        x.append(l[i])
for i in x:
    if i%2==0:
        m=m+1
if m == len(x):
    print("True")
else:
    print("False")