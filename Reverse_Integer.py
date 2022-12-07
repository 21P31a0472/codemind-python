n=int(input())
i=n
if n<0:
    n=-n
rev=0
while n:
    rev=rev*10+n%10
    n=n//10
if i<0:
    print(-rev)
else:
    print(rev)