class Solution:
     def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        def fun(s,i):
            if (i>=len(s)/2):
                return s
            s[i],s[len(s)-i-1]=s[(len(s))-i-1],s[i]
            fun(s,i+1)
        fun(s,i)
 