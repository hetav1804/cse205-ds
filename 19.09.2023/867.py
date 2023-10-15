class Solution:
    
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp=[]
        ans=[]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            ans.append(temp)
            temp=[]
        return ans
        