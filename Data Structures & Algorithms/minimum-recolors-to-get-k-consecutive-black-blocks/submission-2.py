class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0;
        count = 0;
        min_recolors = float('inf')

        for i in range(len(blocks)):
            if blocks[i] == "W":
                count += 1;
            
            if i - left + 1 == k:
                min_recolors = min(count,min_recolors)
                if blocks[left] == "W":
                    count -= 1
                left += 1
        return min_recolors;
        