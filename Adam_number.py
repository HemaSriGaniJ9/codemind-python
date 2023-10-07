a = int(input())
b = a*a
s=0
t=a
while t!=0:
    r=t%10
    s=s*10+r
    t=t//10
c=s*s
t2=c
s1=0
while t2!=0:
    r1=t2%10
    s1=s1*10+r1
    t2=t2//10
if b==s1:
    print("True")
else:
    print("False")