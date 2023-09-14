a = int(input())
flag=False
for i in range(1,a):
    s=i*(i+1)
    if a==s:
        flag=True
        break
    else:
        flag=False
if flag==True:
    print("YES")
else:
    print("NO")