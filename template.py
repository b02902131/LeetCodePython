class Solution:
    def methodName(self, n: int) -> List[str]:

class TestCase(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y  

class TestCase(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y  
              
testCases = [
    TestCase(0,1),
    TestCase(0,1),
    TestCase(0,1),
]

if __name__ == "__main__":
    
    s = Solution()
    
    ac = True
    for tc in testCases:
        if s.methodName(tc.x) != tc.y:
            ac = False
            print(f'wrong! {tc.x}, {tc.y}, a = {s.methodName(tc.x)}')

    if ac:
        print('All correct!')