a = int(input())
lst =[]
c=0
while a!=0:
    r=a%10
    c+=1
    if r not in lst:
        lst.append(r)
    a=a//10
x=len(lst)
if c==x:
    print("Unique Number")
else:
    print("Not Unique Number")