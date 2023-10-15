class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        #for i in range(1,len(nums)+1):
        print(len(nums))
        if len(nums)==0 or len(nums)==1 or len(nums)==2:
            return -1
        else:
            return nums[1]
        
        