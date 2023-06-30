class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_ = -1
        for _ in range(len(arr)-1, -1, -1):
            temp = arr[_]
            arr[_] = max_
            max_ = max(temp, max_)
        
        return arr
