
import math
import sys

class Solution:
    def calculateEntropy(self, input) -> float:
        # return math.log(2, 5)
        # return log(2, 1)
        
        dict = {}
        for i in range(len(input)):
            if input[i] in dict:
                dict[input[i]] += 1
            else:
                dict[input[i]] = 1
        
        entropy = 0
        for key in dict:
            # P(xi) = dict[input[i]] / len(input)
            # entropy += - P(xi) * log2 (P(xi))
        
            prop = dict[key] / len(input)
            if prop == 1:
                return 0
            # print(prop * math.log(2, prop))
            entropy += - prop * math.log(prop, 2)
        
        return entropy
    
if __name__ == "__main__":
    s = Solution()
    ans = s.calculateEntropy([1,2,3,4,5,6])
    
    print(ans)
    print(s.calculateEntropy([1, 2, 6, 7, 9, 10]))
    print(s.calculateEntropy([1,2,3,4,5,6,7,8,9,10]))