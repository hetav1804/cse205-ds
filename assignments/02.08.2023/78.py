class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def help(ar,o,r):

            if len(ar)==0:
                r.append(o)
                return
            o1 = o[:]
            o2 = o[:]
            o2.append(ar[0])
            help(ar[1:],o1,r)
            help(ar[1:],o2,r)
            return
        r=[]
        o=[]
        help(nums,o,r)
        return r