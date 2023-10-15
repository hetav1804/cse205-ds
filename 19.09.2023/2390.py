class Solution:
    def removeStars(self, s: str) -> str:
        x=[]
        for i in range(len(s)):
            x.append(s[i])
            if s[i]=='*':
                x.pop()
                if len(x)!=0:
                    x.pop()
        z="".join(x)
        #print(z)
        return z