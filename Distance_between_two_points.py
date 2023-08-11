import math
a=int(input())
b=int(input())
c=int(input())
d=int(input())
x=((a-c)*(a-c)+(b-d)*(b-d))
y=math.sqrt(x)
print(f"{y:.4f}")