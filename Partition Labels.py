# https://leetcode.com/problems/partition-labels/
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.


# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.


class Solution:
    def partitionLabels(self, s: str):

        # we need to know all ends for each letter in advance.

        ends = {}
        for i, x in enumerate(s):
            ends[x] = i

        result = []

        i = 0
        while(i < len(s)):
            end_location = ends[s[i]]
            length = 0

            while(i <= end_location):
                length += 1

                if ends[s[i]] > end_location:
                    end_location = ends[s[i]]

                i += 1

            result.append(length)

        return result
