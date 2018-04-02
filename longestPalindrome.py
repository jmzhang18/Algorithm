# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    string_length = len(s)
    
    table = [[0 for i in range(string_length)] for j in range(string_length)]
    
    max_string_length = 1
    start_i = 0
    '''
        for substring with only one char
    '''
    for i in range(string_length):
        table[i][i] = True
        
    # for substring with two char
    for i in range(string_length-1):
        if (s[i]==s[i+1]):
            max_string_length = 2
            table[i][i+1] = True
            start_i = i

    # all other substring
    substring_length = 3
    while (substring_length <= string_length):
        for i in range(string_length-substring_length+1):
            j = i + substring_length - 1
            if (table[i+1][j-1] and (s[i]==s[j])):
                table[i][j] = True
                if (substring_length > max_string_length):
                    start_i = i
                    max_string_length = substring_length
        substring_length += 1
    end_i = start_i + max_string_length
    return s[start_i:end_i]