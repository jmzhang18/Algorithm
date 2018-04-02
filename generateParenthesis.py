class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def parTree(p, left, right, ret=[]):
            if (left>0):
                parTree(p+'(', left-1, right)
            if (right>left):
                parTree(p+')', left, right-1)
            if (right==0 and left==0):
                ret.append(p)
            return ret
        
        ret =parTree('', n, n)
        # print(ret)
        return ret

s = Solution()
s.generateParenthesis(3)
