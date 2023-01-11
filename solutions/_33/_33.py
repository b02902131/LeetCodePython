from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minimumIndex = self.findMinimumIndex(nums)
        leftIndex = self.binarySearch(nums, target, 0, minimumIndex - 1)
        rightIndex = self.binarySearch(nums, target, minimumIndex, len(nums) - 1)
        return max(leftIndex, rightIndex)
        
    def bruteForce(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1

    def findMinimumIndex(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return 0
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return left
    
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            middle = (left + right) // 2
            middleValue = nums[middle]
            if target == middleValue:
                return middle
            elif target > middleValue:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    
# s = Solution()
# ans = s.search([4,5,6,7,0,1,2], 0)
# print(ans)
