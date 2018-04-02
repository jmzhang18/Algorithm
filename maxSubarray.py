class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==0):
            return None
        general_max = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max+nums[i])
            general_max = max(current_max, general_max)
        return general_max
            