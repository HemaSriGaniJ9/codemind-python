a = int(input())
x = list(map(int,input().split()))
k=[]
for i in x:
    if i%2!=0:
        k.append(i)
for i in x:
    if i%2==0:
        k.append(i)
for j in k:
    print(j,end=" ")