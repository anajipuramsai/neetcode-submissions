class Solution:
    def search(self, nums: List[int], target: int) -> int:
        values = set()

        for i in range(len(nums)):
            values.add(nums[i])

            if target in values:
                return i
            
        return -1  