n=int(input())
l=list(map(int,input().split()))
k,s=map(int,input().split())
c=[]
for i in l:
    if i<k or i>s:
        c.append(i)
print(sum(c))
    
    