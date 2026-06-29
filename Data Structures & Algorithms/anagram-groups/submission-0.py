class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
    
        for word in strs:
            
            letters = {}
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
        
            key = tuple(sorted(letters.items()))
            
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())