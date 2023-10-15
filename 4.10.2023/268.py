class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        sum=0
        sum1=0
        for i in range(1,len(nums)+1):
            sum=sum+i
        print(sum)
        for i in nums:
            sum1+=i
        return sum-sum1