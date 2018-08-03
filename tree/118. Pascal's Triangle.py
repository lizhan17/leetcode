class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # dp
        
        if numRows == 1:
            return [[1]]
        tri =[[] for i in range(numRows)] # init tri
        tmp = [0 for i in range(numRows)]
        for row in range(numRows):
           
            tri[row] = tmp
            for i in range(numRows): # 0 1 2 3 4
                if i == 0:
                    tmp[row][i]= 1
                if i == numRows-1: #  i ==4 @numrows==5
                    tri[row][i]= 1 
                if i>0 and i< numRows-1:  #  0<i<4 @numrows ==4  i=1 row=4
                    tri[row][i] = tri[row-1][i-1]+ tri[row-1][i]    # tmp[2] row5, the third == tri[3][1]+ tri[3][2]
        return tri
    # ref leetcode
    def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
