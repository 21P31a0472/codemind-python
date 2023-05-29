n=int(input())
h=n
rev=0
while n:
    p=n%10
    rev = rev*10 + p
    n = n // 10
if h == rev:
    print("True")
else:
    print("False")
    