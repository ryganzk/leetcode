class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True
        
        if len(t) != 0:
            x = 0
            for y in range(len(t)):
                if s[x] == t[y]:
                    x += 1
                    if (x == len(s)):
                        return True

        return False
        