from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, target, path):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return res


        
        # self.ans = []
        # candidates.sort()
        # self.combinationSumHelper(candidates, target, [])
        # return self.ans

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