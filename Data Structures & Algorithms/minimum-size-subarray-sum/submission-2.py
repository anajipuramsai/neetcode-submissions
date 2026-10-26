class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        value = 0
        min_window = float('inf')


        for i in range(len(nums)):

            value = value + nums[i]

            while value >= target:
                min_window = min(min_window, i - left + 1)
                value -= nums[left]
                left += 1
        if min_window == float('inf'):
            return 0
        return min_window