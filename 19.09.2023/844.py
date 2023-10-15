class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x=[]
        y=[]
        for i in range(len(s)):
            x.append(s[i])
            if s[i]=='#':
                x.pop()
                if len(x)!=0:
                    x.pop()
        
        for j in range(len(t)):
            y.append(t[j])
            if t[j]=='#':
                y.pop()
                if len(y)!=0:
                    y.pop()
        
        return x==y