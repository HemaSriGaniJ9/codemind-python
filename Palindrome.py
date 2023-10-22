a = int(input())
n=a
s=0
while a>0:
    r=a%10
    s=s*10+r
    a=a//10
if(n==s):
    print("True")
else:
    print("False")