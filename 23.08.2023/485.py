class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        temp=0

        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                if(temp<=cnt):
                    temp=cnt
                cnt=0
        if(cnt>=temp):
            return cnt
        else:
            return temp
