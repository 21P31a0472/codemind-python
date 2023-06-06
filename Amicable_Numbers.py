n = int(input())
m = int(input())
k = 0
l = 0
for i in range(1,(n//2)+1):
    if n%i == 0:
        k+=i
for j in range(1,(m//2)+1):
    if m%j == 0:
        l+=j
if n == l and m == k :
    print("Amicable")
else:
    print("Not Amicable")