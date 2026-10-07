class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_dict = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in sorted_dict:
                sorted_dict[key].append(word)
            else:
                sorted_dict[key] = [word]

        return list(sorted_dict.values())