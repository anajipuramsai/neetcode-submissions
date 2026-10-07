class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}

        for i in range(len(nums)):
            dictionary[nums[i]] = dictionary.get(nums[i],0) + 1

        return max(dictionary, key=dictionary.get)