"""
important trick 

with dictionary in python


more quick way 


get the sum of set (why we use set):
we just know they are 2 and 1 is 1








"""


## my solution beat only 3%
## use dictions as datastructure
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
            
            
 ## then I use set of python
 ## and get the total sum of nums list
 ## again only beats 10%
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_of_nums = set(nums)
        sum_set = 0
        sum_nums = 0
        for set_num in set_of_nums:
            sum_set += set_num
        for num in nums:
            sum_nums += num
        return 2*sum_set - sum_nums
