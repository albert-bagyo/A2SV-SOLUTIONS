class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = Counter(s)
        for let in t:
            if let not in s:
                return let
            elif t_count[let] != s_count[let]:
                return let
