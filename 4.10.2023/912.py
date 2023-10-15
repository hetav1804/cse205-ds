class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left, right = arr[:mid], arr[mid:]
            left, right = merge_sort(left), merge_sort(right)
            result, i, j = [], 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            print(result)
            print("*")
            result.extend(left[i:])
            print(result) 
            result.extend(right[j:])
            return result
        return merge_sort(nums)