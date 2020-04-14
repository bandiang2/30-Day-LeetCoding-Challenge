# Day 13

# Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
#	Input: [0,1]
#	Output: 2
#	Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

#	Example 2:
#	Input: [0,1,0]
#	Output: 2
#	Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000.

# Solution

from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        counts = defaultdict(int)
  
        seen = 0
        j = 0
        max_length = 0
        while j < n:
            
            if nums[j] == 0:
                seen += -1
            else:
                seen += 1
                
            if seen == 0:
                max_length = j + 1
            
            if seen in counts:
                c = counts[seen]
                max_length = max(max_length, j - c)
            else:
                counts[seen] = j
            j += 1
                
        return max_length   
        
