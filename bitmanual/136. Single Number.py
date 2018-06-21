"""
linear time complexity
so  you can have stack 


important trick 


sol1:
with dict
5%
sol2:
with set and sum 
10%

sol3:
python list built in functions

-- count
failed very slow 

-- pop 
we can't use pop because pop is O(k) average
pop last is constant time
sol4:
Bitwise XOR

        res = 0
        for ele in nums:
            res ^= ele
        return res






"""


## my solution beat only 5%
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

    
    
    ### 
        res = 0
        for ele in nums:
            res ^= ele
        return res
    # source leetcode
