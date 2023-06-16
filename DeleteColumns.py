class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        if len(strs) == 1:
            return cnt
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j][i] < strs[j - 1][i]:
                    cnt += 1
                    break
        return cnt
