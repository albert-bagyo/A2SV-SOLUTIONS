class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
    
        for word in words[1:]:
            
            counts &= Counter(word)
        
        return list(counts.elements())
