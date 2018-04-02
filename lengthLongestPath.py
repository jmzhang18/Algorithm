'''
Google Interview question on January 20th, 2017

Author: William Zhang
'''
class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        main_stack = list()
        input_string = input
        max_length = 0
        for line in input_string.splitlines():
            name = line.lstrip("\t")               
            level = len(line) - len(name)
            previous_length = 0
            if (level>0):
                previous_length = main_stack[level-1]
            if ('.' in name):
                # check if maximum reached
                max_length = max(max_length, previous_length+len(name))
            else:
                current_length = previous_length + len(name) +1 
                if (level >= len(main_stack)):
                    main_stack.append(current_length)
                else:
                    main_stack[level] = current_length
        return max_length
