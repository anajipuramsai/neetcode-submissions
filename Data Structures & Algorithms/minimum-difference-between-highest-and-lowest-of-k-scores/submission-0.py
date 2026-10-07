class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        left = 0
        minimum_value = float('inf')
        nums.sort()
        diff = 0
        for i in range(len(nums)):
            if i - left + 1 == k:
                diff = nums[i] - nums[left]
                minimum_value = min(minimum_value , diff)
                left += 1

            
        return minimum_value