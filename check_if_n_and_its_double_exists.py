class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for n in arr:
            if n == 0:
                if arr.count(0) > 1:
                    return True
                continue
            if n/2 in arr:
                return True
        return False
