class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        from collections import Counter
        res = []
        count = Counter(nums)
        n = len(nums)

        for num, cnt in count.items():
            if cnt > (n/3):
                res.append(num) 
        
        return res
