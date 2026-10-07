class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            total = 0

            for num in piles:
                total = total + math.ceil(float(num)/mid)

            if total > h:
                left = mid+1
            else:
                right = mid
        return left