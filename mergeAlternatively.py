class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        i = 0
        mini = min(len(word1), len(word2))
        while(i < mini):
            res += word1[i] + word2[i]
            i += 1
        
        return res + word1[i:] + word2[i:]
