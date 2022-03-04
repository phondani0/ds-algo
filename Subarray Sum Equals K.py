# Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums, k) -> int:

        curr_sum = 0
        ans = 0
        dict_ = {0: 1}

        for num in nums:
            curr_sum += num

            if((curr_sum - k) in dict_):
                ans += dict_[curr_sum - k]

            if(curr_sum in dict_):
                dict_[curr_sum] += 1
            else:
                dict_[curr_sum] = 1

        return ans
