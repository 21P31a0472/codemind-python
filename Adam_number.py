n=int(input())
l=n**2
rev1=0
rev2=0
while n:
    p=n%10
    n = n // 10
    rev1 = rev1 * 10 + p
r = rev1 ** 2
while r:
    q =r%10
    r = r // 10
    rev2 = rev2 * 10 + q
if l == rev2:
    print("True")
else:
    print("False")
    
    