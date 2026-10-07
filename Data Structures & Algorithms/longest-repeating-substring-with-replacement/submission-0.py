class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0;
        frequency = {}
        max_length = 0;
        max_frequency = 0

        for i in range(len(s)):
            frequency[s[i]] = frequency.get(s[i],0)+1

            max_frequency = max(max_frequency,frequency[s[i]]);

            while (i - left + 1) - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1 


            max_length = max(max_length,i - left + 1)

        return max_length

        