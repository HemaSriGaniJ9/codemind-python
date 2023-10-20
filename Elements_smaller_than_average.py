a = int(input())
k = list(map(int,input().split()))
b = sum(k)//a
c=0
for i in k:
    if i<=b:
        c+=1
print(c)