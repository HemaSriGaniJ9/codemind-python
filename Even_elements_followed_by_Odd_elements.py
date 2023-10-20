a = int(input())
k = list(map(int,input().split()))
x = []
for i in k:
    if(i%2==0):
        x.append(i)
for i in k:
    if(i%2!=0):
        x.append(i)
for j in x:
    print(j,end=" ")