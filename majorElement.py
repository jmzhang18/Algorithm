#!/usr/bin/env python

'''
The Boyer–Moore majority vote algorithm is an algorithm for finding the majority of a sequence of elements using linear time and constant space.
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         record = dict()
#         max_item = None
#         max_num = 0
#         for i in range(len(nums)):
#             if (nums[i] in record):
#                 record[nums[i]] += 1
#             else:
#                 record[nums[i]] = 1
        
#         for key, val in record.items():
#             if (val > max_num):
#                 max_num = val
#                 max_item = key
#         return max_item

        count = 1
        major = nums[0]
        for i in range(1, len(nums)):
            if (count == 0):
                major = nums[i]
                count = 1
            else:
                if (major == nums[i]):
                    count += 1
                else:
                    count -= 1
        return major
        