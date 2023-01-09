class Solution:
    
    def longestPalindrome(self, s: str) -> str:

        return self.dpMethod(s)
        
        # return self.bruteMethod(s)

    def dpMethod(self, s: str) -> str:
        ans = ""
        n = len(s)
        dp = [[False] * n for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                dp[i][j] = (s[i] == s[j]) and (i - j < 3 or dp[i - 1][j + 1])
                if dp[i][j] and i - j + 1 > len(ans):
                    ans = s[j:i+1]
        return ans

    def bruteMethod(self, s: str) -> str:
        ans = ""
        maxLen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i + 1 <= maxLen:
                    continue
                if self.checkStrIsPalindrome(s[i:j+1]):
                    maxLen = j - i
                    ans = s[i:j+1]
        return ans

    def checkStrIsPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while right >= left:
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        return True