n = int(input())
nums = list(map(int,input().split()))
s=0
s1=0
for i in range(len(nums)):
    if(i%2==0):
        s=s+nums[i]
    else:
        s1=s1+nums[i]
print(abs(s1-s))   