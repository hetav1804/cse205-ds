class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x=[]
        for i in operations:
            if i=="C":
                x.pop()
            elif i=="D":
                j=x[-1]*2
                x.append(j)
            elif i=="+":
                k=x[-1]+x[-2]
                x.append(k)
            else:
                x.append(int(i))
        print(x)

        sum=0
        for j in range(len(x)):
            sum=sum+int(x[j])
        return sum