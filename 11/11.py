class Solution:
    def maxArea(self, height: List[int]) -> int:
        # return self.bruteForce(height)
        return self.methodPointer(height)

    def methodPointer(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxAmount = 0
        while right > left:
            maxAmount = max(maxAmount, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxAmount


    def bruteForce(self, height: List[int]) -> int:
        maxAmount = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                amount = (j - i) * min(height[j],height[i])
                if amount > maxAmount:
                    maxAmount = amount
        return maxAmount