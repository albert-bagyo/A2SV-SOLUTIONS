class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for _ in range(len(nums)):
            n = nums[_]
            nums.append(int(str(n)[::-1]))
        return len(set(nums))
