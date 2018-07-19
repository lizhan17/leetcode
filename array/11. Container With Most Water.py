class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxRes = 0
        for i in range(0,len(height)):
            for j in range(i,len(height)):
                tmp = self.smaller(height[i],height[j])*(j-i)
                if tmp > maxRes:
                    maxRes = tmp 
        return maxRes
            
    def smaller(self,a,b):
        if a<b:
            return a
        else:
            return b
        
