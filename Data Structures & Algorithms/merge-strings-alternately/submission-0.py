class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #   initialize word3
        # append letter from word 1 and word 2
        # if any of the length is over append the remainig all

        word3 = []
        i = 0
        j = 0


        while i < len(word1) and j < len(word2):
            word3.append(word1[i])
            word3.append(word2[j])
            i += 1
            j += 1
        
        word3.append(word1[i:])
        word3.append(word2[j:])

        return "".join(word3)
