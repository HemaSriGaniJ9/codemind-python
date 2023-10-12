n=int(input())
nums=list(map(int,input().split()))
s=sum(nums)//n
if s in nums:
    print("True")
else:
    print("False")