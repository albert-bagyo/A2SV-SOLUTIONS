class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        l = len(nums)
        while 0 in nums[:l - k]:
            nums.remove(0)
            nums.append(0)
            k += 1
