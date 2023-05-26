n=int(input())
l=list(map(int,input().split()))
ep=[]
for i in l:
    if i%2 == 0:
        ep.append(i)
for i in l:
    if i%2 != 0:
        ep.append(i)
print(*ep)