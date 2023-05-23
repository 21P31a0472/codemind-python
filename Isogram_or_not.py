n=input()
d={}
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d.values():
    if i!=1:
        print("False")
        break
else:
    print("True")