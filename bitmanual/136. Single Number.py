"""
important trick 

with dictionary in python


more quick way 


get the sum of set (why we use set):
we just know they are 2 and 1 is 1








"""


## beat only 3%
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict ={}
        
        for num in nums:
            if num not in dict:
                dict[num]=1  # init
            else: # add one
                dict[num]= dict[num]+1
                
        for unique_num in dict:
            if dict[unique_num]==1:
                return unique_num
class Solution(object):
    def singleNumber(self, nums):
        
