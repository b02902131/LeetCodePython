class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {')':'(', '}':'{', ']':'['}
        brackets = []
        for i in range(len(s)):
            c = s[i]
            if c not in bracketsMap:
                brackets.append(c)
            else:
                if len(brackets) <= 0:
                    return False
                lastBracket = brackets.pop()
                if lastBracket != bracketsMap[c]:
                    return False
        if len(brackets) > 0:
            return False
        return True