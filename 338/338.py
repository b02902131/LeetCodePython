from math import *


class Solution:
    def countBits(self, num: int):
        ans = [0]
        ptr = 0
        prePow = 1
        curPow = 1

        while ptr < num:
            ptr += 1
            if ptr == curPow:
                prePow = curPow
                curPow *= 2
                ans += [1]
            else:
                ans += [1 + ans[ptr - prePow]]

        return ans


s = Solution()
print(s.countBits(50))
