n=int(input())
l1=[]
for i in range(n):
    li=list(map(int,input().split()))
    l1.append(li)
l2=[]
for i in range(n):
    li=list(map(int,input().split()))
    l2.append(li)
d=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(abs(l1[i][j]-l2[i][j]))
    d.append(a)
for i in range(n):
    s=""
    for j in range(n):
        s=s+str(d[i][j])+" "
    s=s[0:len(s)-1]
    print(s)