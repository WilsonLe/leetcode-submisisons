# https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1, nums2): 
        # A is the shorter array of the 2
        A, B = nums1, nums2
        if len(A) > len(B):
          A, B = B, A

        totalElement = len(A) + len(B)
        halfElement = totalElement // 2
        
        # A's left and right index pointer
        l, r = 0, len(A) - 1
        
        while True:
          i = (l + r) // 2 # index ptr
          j = halfElement - i - 2
                     
          # right most value of left partition
          Aleft = A[i] if i >= 0 else float('-inf')
          Bleft = B[j] if j >= 0 else float('-inf')
          
          # left most value of right partition
          Aright = A[i + 1] if i + 1 < len(A) else float('inf')
          Bright = B[j + 1] if j + 1 < len(B) else float('inf')
          
          if Aleft <= Bright and Bleft <= Aright:
            # if odd 
            if totalElement % 2:
              return min(Aright, Bright)
            # if even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
          else:
            if Aleft > Bright:
              r = i - 1
            else:
              l = i + 1
          
print(Solution().findMedianSortedArrays([1,2,3], [4,5,6]))