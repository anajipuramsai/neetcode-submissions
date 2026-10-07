class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
        map = {}

        for i in range(len(numbers)):
            map[numbers[i]] = i + 1

        for i in range(len(numbers)):
            temp = target - numbers[i]

            if temp in map and map[temp] != i:
                return [i + 1, map[temp]]