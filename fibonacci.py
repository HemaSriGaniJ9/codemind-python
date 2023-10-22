a = int(input())
b=-1
c=1
for i in range(a):
    d=b+c
    b=c
    c=d
    print(c,end=' ')