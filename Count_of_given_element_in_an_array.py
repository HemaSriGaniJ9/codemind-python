n = int(input())
nums = list(map(int,input().split()))
se = int(input())
c=0
for i in range(len(nums)):
    if(nums[i]==se):
        c+=1
print(c)
    