# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results: List[List[int]] = []

        def dfs(curTotal: int, curComb: List[int], start: int):
            if curTotal == target:
                results.append(curComb[:])
                return
            if curTotal > target:
                return
            for i in range(start, len(candidates)):
                curComb.append(candidates[i])
                curTotal += candidates[i]
                dfs(curTotal, curComb, i)
                curTotal -= curComb.pop()
        dfs(0, [], 0)
        return results


assert (Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]])
assert (Solution().combinationSum([2, 3, 5], 8) == [
    [2, 2, 2, 2], [2, 3, 3], [3, 5]])
assert (Solution().combinationSum([2], 1) == [])
