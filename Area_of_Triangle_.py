a,b,c=map(int,input().split())
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
b=d**0.5
print(f"{b:.2f}")