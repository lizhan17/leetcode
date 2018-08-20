'''
ref leetcode

for x in s is the 


'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1 or numRows >= len(s):
            return s
        L =['']*numRows
        index,step = 0,1
        for x in s:    # typically it is the start
            L[index] += x # put x in each row index
            if index == 0: # index may change
                step =1
            elif index == numRows -1:
                step =-1
            index += step
            
        return ''.join(L)
        
