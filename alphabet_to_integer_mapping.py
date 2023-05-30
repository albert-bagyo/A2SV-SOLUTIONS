class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        ind = -1
        map_ind = 0
        while ind >= -len(s):
            if s[ind] == '#':
                map_ind = int(s[ind - 2:ind])
                ind -= 3
            else:
                map_ind = int(s[ind])
                ind -= 1
            res = chr(96 + map_ind) + res

        return res
