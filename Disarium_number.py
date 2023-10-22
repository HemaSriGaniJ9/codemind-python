a = int(input())
k=str(a)
d=len(k)
q=a
s=0
while a!=0:
    r=a%10
    s=s+(r**d)
    a=a//10
    d=d-1
if(s==q):
    print("True")
else:
    print("False")