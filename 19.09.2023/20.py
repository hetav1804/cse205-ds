class Solution:
    def isValid(self, s: str) -> bool:
        dict={
            '(':')',
            '[':']',
            '{':'}'
        }
        x=[]
        for i in s:
            if i in dict:
                x.append(i)
            elif len(x)==0 or i!=dict[x.pop()]:
                return False
        return len(x)==0
        