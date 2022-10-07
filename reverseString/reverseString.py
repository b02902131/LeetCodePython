from ast import List


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return s
        
        x = self.reverseString(s[1:])
        s[:] = s[:1] + x[:]
        temp = s.pop(0)
        s.append(temp)
        return s
        
        
if __name__ == "__main__":
    
    s = Solution()
    x = [1,2,3,4,5]
    
    # print(x)
    s.reverseString(x)
    # print(x)
    
    