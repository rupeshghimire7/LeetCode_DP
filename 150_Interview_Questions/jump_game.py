"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        # Initially, goal is last index, say 3
        for i in range(len(nums))[::-1]:
            #i. if i=3 and num[3] = 3, => 3+3>=3 so goal =i = 3
            #ii. if i=2 and nums[2]=1  => 2+1 >= 3 so goal = i = 2
            #iii. if i=1 and nums[1]=0 => 1+0 !>= 2 so unchanged goal = 2
            #iv. if i=0 and nums[0]=1  => 0+1 !>= 2 so unchanged goal=2
            # bool goal = True so notGoal = False

            if i+nums[i]>=goal:
                goal = i
        return not goal
