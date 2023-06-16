class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
        
        return list(filter(lambda num: num != 0, nums))+ ([0] * count)
