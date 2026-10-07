class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in sorted_dict:
                sorted_dict[key].append(s)
            else:
                sorted_dict[key] = [s]

        return list(sorted_dict.values())