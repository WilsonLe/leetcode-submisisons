# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(i):
            if i == len(nums):
                output.append(nums[:])
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return output


print(Solution().permute([1, 2, 3]))
assert (Solution().permute([1, 2, 3]) == [[1, 2, 3], [
        1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
assert (Solution().permute([0, 1]) == [[0, 1], [1, 0]])
assert (Sodfution().permute([1]) == [[1]])
