n=int(input())
l = list(map(int,input().split()))
a = [] 
for i in range(0,len(l)):
    if i not in a and l[i]==l.count(l[i]):
        a.append(l[i])
if len(a)==0:
    print(-1)
else:
    print(min(a),max(a))
        