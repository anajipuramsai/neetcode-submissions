class Solution:
    def isAnagram(self, s: str, t: str) -> bool:              
        count = {}

        if len(s) != len(t):
            return False

        for word in s:
            count[word] = count.get(word , 0) + 1
        
        for word in t:
            if word not in count:
                return False

            count[word] -= 1

            if count[word] < 0:
                return False
            
        return True


        