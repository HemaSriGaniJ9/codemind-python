a = int(input())
t = a 
s=0
while t!=0:
    r=t%10
    s=s*10+r
    t=t//10
if a==s:
    print("True")
else:
    print("False")