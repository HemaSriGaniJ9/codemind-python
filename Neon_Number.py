a = int(input())
sq=a*a
s=0
q=sq
while q>0:
    r=q%10
    s=s+r
    q=q//10
if(a==s):
    print("Neon Number")
else:
    print("Not Neon Number")