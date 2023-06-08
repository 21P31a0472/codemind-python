n = int(input())
l = list(map(int,input().split()))
k = int(input())
e = []
for i in range(n):
    if l.count(l[i]) == k and l[i] not in e:
        e.append(l[i])
if len(e)==0:
    print("-1")
else:
    print(*e)