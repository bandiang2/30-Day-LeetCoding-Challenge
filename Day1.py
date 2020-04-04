# Day 1

#### SINGLE NUMBER

#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

#Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example: 
#        Input: [2,2,1]
#        Output: 1

# SOLUTION

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_elt = {}
        for item in nums:
            if item in count_elt:
                count_elt[item] += 1
            else:
                count_elt[item] = 1
                
        for key, value in count_elt.items():
            if value == 1:
                return key
