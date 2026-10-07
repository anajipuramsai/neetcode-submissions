class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        value = 0
        min_length = float('inf')

        for i in range(len(nums)):
            value += nums[i]

            while value >= target:
                min_length = min(min_length, i - left + 1)
                value -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        return min_length