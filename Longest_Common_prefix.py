class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def similar(res, word):
            r = ""
            for i in range(min(len(res), len(word))):
                if res[i] != word[i]:
                    break
                r += res[i]
            return r

        res = strs[0] if len(strs) != 0 else ""
        for word in strs:
            if res == "":
                return res
            res = similar(res, word)
        return res
