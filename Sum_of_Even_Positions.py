n=int(input())
x=list(map(int,input().split()))
z=x[0:len(x):2]
print(sum(z))