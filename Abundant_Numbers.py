n=int(input())
l=[]
for i in range(1,n):
     if n % i == 0 :
         l.append(i)
k =sum(l)
if k > n:
    print("True")
else:
    print("False")
         