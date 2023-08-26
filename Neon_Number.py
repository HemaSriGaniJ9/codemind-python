a = int(input())
s=0
b=a*a
while b>0:
    d=b%10
    s=s+d
    b=b//10
if(s==a):
    print("Neon Number")
else:
    print("Not Neon Number")

