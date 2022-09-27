# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, j, start, end = 0, len(nums) - 1, -1, -1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                m, n = mid, j
                while m <= n:
                    end = (m + n) // 2
                    if end >= len(nums) - 1:
                        break
                    if nums[end] == target and nums[end + 1] == target:
                        m = end + 1
                    elif nums[end] == target and nums[end + 1] != target:
                        break
                    elif nums[end] != target and nums[end + 1] != target:
                        n = end - 1
                a, b = i, mid
                while a <= b:
                    start = -((a + b) // -2)  # ceil division
                    if start <= 0:
                        break
                    if nums[start] == target and nums[start - 1] == target:
                        b = start - 1
                    elif nums[start] == target and nums[start - 1] != target:
                        break
                    elif nums[start] != target and nums[start - 1] != target:
                        a = start + 1
                break
            else:
                if nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
        return [start, end]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        a, b = -1, -1
        if len(nums) == 0:
            return [a, b]
        if nums[0] == target:
            a = 0
        if nums[-1] == target:
            b = len(nums) - 1

        # first binary search for bottom index
        i, j = 0, len(nums) - 1

        while i <= j and a == -1:
            mid = (i + j) // 2
            if nums[mid] == target and nums[mid - 1] != target:
                a = mid
            elif nums[mid] == target and nums[mid - 1] == target:
                j = mid - 1
                continue
            elif nums[mid] > target:
                j = mid - 1
                continue
            else:
                i = mid + 1

        # first binary search for bottom index
        i, j = 0, len(nums) - 1

        while i <= j and b == -1:
            mid = (i + j) // 2
            if nums[mid] == target and nums[mid + 1] != target:
                b = mid
            elif nums[mid] == target and nums[mid - 1] == target:
                i = mid + 1
                continue
            elif nums[mid] > target:
                j = mid - 1
                continue
            else:
                i = mid + 1

        return [a, b]


assert (Solution().searchRange2([1, 2, 3], 2) == [1, 1])
assert (Solution().searchRange2([2, 2], 2) == [0, 1])
assert (Solution().searchRange2([5, 7, 7, 8, 8, 10], 8) == [3, 4])
assert (Solution().searchRange2([1], 1) == [0, 0])
assert (Solution().searchRange2([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
assert (Solution().searchRange2([], 0) == [-1, -1])

assert (Solution().searchRange([1, 2, 3], 2) == [1, 1])
assert (Solution().searchRange([2, 2], 2) == [0, 1])
assert (Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])
assert (Solution().searchRange([1], 1) == [0, 0])
assert (Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
assert (Solution().searchRange([], 0) == [-1, -1])
