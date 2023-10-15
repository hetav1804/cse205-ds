class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        min_diff = 100
        arr.sort()
        result = []
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff

                result = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                print(result)
                result.append([arr[i], arr[i+1]])
        
        return result
        