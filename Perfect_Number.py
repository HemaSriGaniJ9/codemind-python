q = int(input())
f=0
for i in range(1,q):
    if(q%i==0):
        f=f+i
if(q==f):
    print("True")
else:
    print("False")
    