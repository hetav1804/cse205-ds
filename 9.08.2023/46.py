lass Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def solve(s, nums):

            if len(s) == len(nums):
                res.append(s)
                return

            for i in range(len(nums)):
                if nums[i] not in s:
                    solve(s + [nums[i]], nums)


        res=[]
        solve([], nums)
        return res