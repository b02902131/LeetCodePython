class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        for interval in intervals:
            if len(result) == 0 or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
        return result

        
