# Day 6

# Group Anagrams

# Given an array of strings, group anagrams together.

# Example

#	Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#	Output:
#	[
#	  ["ate","eat","tea"],
#	  ["nat","tan"],
#	  ["bat"]
#	]

# Note:

#	All inputs will be in lowercase.
#	The order of your output does not matter.

### My Solution 

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for s in strs:
            inter_s = tuple(sorted(s))
            if inter_s in anagrams:
                anagrams[inter_s].append(s)
            else:
                anagrams[inter_s] = [s]
        return list(anagrams.values())
