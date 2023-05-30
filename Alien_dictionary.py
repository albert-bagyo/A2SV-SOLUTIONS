class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
            def less(word1, word2):
                if len(word1) == 0 and len(word2) != 0:
                    return True
                elif len(word1) != 0 and len(word2) == 0:
                    return False
                elif len(word1) == 0 and len(word2) == 0:
                    return False

                word1_let = order.find(word1[0])
                word2_let = order.find(word2[0])

                if word1_let > word2_let:                 
                    return False
                elif word1_let < word2_let:
                    return True
                else:
                    return less(word1[1:],word2[1:])
            
            for i in range(len(words) - 1):
                if less(words[i + 1] , words[i]):
                    return False
            return True
