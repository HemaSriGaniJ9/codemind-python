n = int(input())
nums = list(map(int,input().split()))
b = 0
for i in range(len(nums)):
    if nums[i]%2!=0:
        b=i
print(b)