from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.combinationSumHelper(candidates, target, [])
        return self.ans

    def combinationSumHelper(self, candidates: List[int], target: int, arr: List[int]) -> List[List[int]]:
        
        print(candidates, target, arr)
        
        if not candidates or target < 0:
            return False

        candidate = candidates[0]

        if target == candidate:
            self.ans.append(arr + [candidate])
            return

        # Get answer with i-th element
        self.combinationSumHelper(candidates, target - candidate, arr + [candidate])
            
        # Get answer with (i+1)-th element
        self.combinationSumHelper(candidates[1:], target, arr)

s = Solution()

ans = s.combinationSum([2,3,6,7], 7)
print(ans)