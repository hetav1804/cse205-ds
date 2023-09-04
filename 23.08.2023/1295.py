class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt=0
        for i in range(0,len(nums)):
            k=nums[i]
            j=str(k)
            if (len(j)%2==0):
                cnt+=1
        return cnt
