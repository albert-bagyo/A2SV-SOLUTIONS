class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse= True)
        max = 0
        l = len(piles)
        n = l // 3
        for i in range(1,l-n,2):
            max += piles[i]
        return max
