class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        i = 0
        j = len(s) - 1

        while i < j:

            # Skip spaces and punctuation from the left
            if not s[i].isalnum():
                i += 1
                continue

            # Skip spaces and punctuation from the right
            if not s[j].isalnum():
                j -= 1
                continue

            # Compare characters
            if s[i] != s[j]:
                return False

            # Move both pointers
            i += 1
            j -= 1

        return True
