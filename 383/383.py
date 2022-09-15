class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for c in ransomNote:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
        for c in magazine:
            if c in dict: 
                dict[c] -= 1
                
        for key in dict:
            if dict[key] > 0:
                return False
                
        return True

class TestCase(object):
    def __init__(self, ransomNote: str, magazine: str, output: bool):
        self.ransomNote = ransomNote
        self.magazine = magazine
        self.output = output
              
testCases = [
    TestCase("a","b", False),
    TestCase("aa","ab", False),
    TestCase("aa","aab", True),
]

if __name__ == "__main__":
    
    s = Solution()
    
    ac = True
    for tc in testCases:
        if s.canConstruct(tc.ransomNote, tc.magazine) != tc.output:
            ac = False
            print(f'wrong! {tc.ransomNote}, {tc.magazine}, a = {s.canConstruct(tc.ransomNote)}')

    if ac:
        print('All correct!')