class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num = n;
        while num % 2 != 0:
            num += num
        return num
