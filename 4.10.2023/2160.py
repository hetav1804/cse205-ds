class Solution:
    def minimumSum(self, num: int) -> int:
        arr=[]
        while num>0:
            arr.append(num%10)
            num=num//10
            #print(num)

        arr.sort()
        a=arr[0] * 10 + arr[-1]
        #print(a)
        
        b=arr[1] * 10 + arr[-2]
        return a+b