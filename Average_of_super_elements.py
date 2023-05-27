n=int(input())
a=[]
l=list(map(int,input().split()))
for i in l:
    if i==l.count(i) and i not in a:
        a.append(i)
if len(a)!=0:
    print("{:.2f}".format(sum(a)/len(a)))
else:
    print(-1)