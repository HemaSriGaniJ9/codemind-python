n = int(input())
nums = list(map(int,input().split()))
s=0
s1=0
for i in nums:
    if(i%2==0):
        s+=i
    else:
        s1+=i
print(f"{abs(s-s1)}")
        

