# https://leetcode.com/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results: List[List[int]] = []
        candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def dfs(curTotal: int, curComb: List[int], start: int):
            if curTotal == n and len(curComb) == k:
                results.append(curComb[:])
                return

            if curTotal > n:
                return

            if (len(curComb) > k):
                return

            if (len(curComb) < k):
                for i in range(start, len(candidate)):
                    curTotal += candidate[i]
                    curComb.append(candidate[i])
                    dfs(curTotal, curComb, i + 1)
                    curTotal -= curComb.pop()

        dfs(0, [], 0)

        return results


assert (Solution().combinationSum3(3, 7) == [[1, 2, 4]])
assert (Solution().combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
assert (Solution().combinationSum3(4, 1) == [])
