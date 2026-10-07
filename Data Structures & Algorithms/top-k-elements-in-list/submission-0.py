class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        indices = {}
        
        for num in nums:
            indices[num] = indices.get(num,0)+1

        sorted_indices = sorted(indices.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in sorted_indices[:k]]