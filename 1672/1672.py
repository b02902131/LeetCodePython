from typing import List
from unittest import TestCase

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for account in accounts:
            wealth = 0
            for m in account:
                wealth += m
            if wealth >= max:
                max = wealth
        return max
    
class TestCase():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
testCases = [
    TestCase([[1,2,3],[3,2,1]], 6),
    TestCase([[1,5],[7,3],[3,5]], 10),
    TestCase([[2,8,7],[7,1,3],[1,9,5]], 17)
]
    
if __name__ == "__main__":
    
    s = Solution()
    
    ac = True
    
    for tc in testCases:
        if s.maximumWealth(tc.x) != tc.y :
            ac = False
            print (f'{tc.x}, {tc.y}, a = {s.maximumWealth(tc.x)}')
            
    if ac: 
        print ('All correct!')