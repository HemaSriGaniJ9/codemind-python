a = int(input())
s=0
for i in range(1,a):
    if(a%i == 0):
        s=s+i
print(f"{s}")
    