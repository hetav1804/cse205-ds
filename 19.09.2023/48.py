class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for k in range(len(matrix)):
            for j in range(len(matrix)-1, -1, -1):
                matrix[k].append(matrix[j].pop(0))