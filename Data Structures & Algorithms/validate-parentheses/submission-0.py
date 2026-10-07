class Solution:
    def isValid(self, s: str) -> bool:
        record = []
        dic = {
            "}" : "{",
            "]" : "[",
            ")" : "("
            }

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                record.append(s[i])
            else:
                if not record:
                    return False
                if record[-1] != dic[s[i]]:
                    return False
                record.pop()
        return len(record) == 0


            
