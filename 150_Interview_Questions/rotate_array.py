'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k<0:
            k += len(nums)
        self.reverse(nums,0,len(nums)-k-1)
        self.reverse(nums,len(nums)-k,len(nums)-1)
        self.reverse(nums,0,len(nums)-1)
        
    def reverse(self,nums,i,j):
        li = i
        ri = j

        while li<ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp
        
            li += 1
            ri -= 1

