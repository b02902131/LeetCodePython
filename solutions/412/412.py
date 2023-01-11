from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz = 0
        buzz = 0
        arr = []
        for i in range(n):
            fizz+=1
            buzz+=1
            if fizz % 3 == 0 and buzz % 5 == 0:
                arr.append("FizzBuzz")
                fizz = 0
                buzz = 0
            elif fizz % 3 == 0:
                arr.append("Fizz")
                fizz = 0
            elif buzz % 5 == 0:
                arr.append("Buzz")
                buzz = 0
            else:
                arr.append(str(i+1))
        return arr
    
class TestCase(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y  
    
testCases = [
    TestCase(3,["1","2","Fizz"]),
    TestCase(5,["1","2","Fizz","4","Buzz"]),
    TestCase(15,["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]),
]

if __name__ == "__main__":
    
    s = Solution()
    
    ac = True
    for tc in testCases:
        if s.fizzBuzz(tc.x) != tc.y:
            ac = False
            print(f'wrong! {tc.x}, {tc.y}, a = {s.fizzBuzz(tc.x)}')

    if ac:
        print('All correct!')