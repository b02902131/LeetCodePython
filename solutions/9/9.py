# my first try
# class Solution(object):
#     def isPalindrome(self, x):
#         s = str(x)
#         for i in range(int(len(s)/2)):
#             if s[i] != s[len(s)-1-i]:
#                 return False
#         return True

# example solution
class Solution (object):
    def isPalindrome(self, x):

        if x<0 or (x%10 ==0 and x !=0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x /= 10

        return x == revertedNumber or x == revertedNumber / 10

class TestCase(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
testCases = [
    TestCase(121, True),
    TestCase(-121, False),
    TestCase(10, False)
]

if __name__ == "__main__":

    s = Solution()
    
    ac = True
    for tc in testCases:
        if s.isPalindrome(tc.x) != tc.y:
            ac = False
            print(f'{tc.x}, {tc.y}')

    if ac:
        print('All correct!')