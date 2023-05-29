n=(input())
l=[]
c=0
for i in (n):
    l.append(int(i))
for i in range(len(l)):
    c=c+(l[i]**(i+1))
if c == int(n):
    print("True")
else:
    print("False")