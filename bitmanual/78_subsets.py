
“”“
Difficulty: medium
date: 2018/06/18
state: done,in 2 hours
rank: beat 33%

general python tech:
short circuit

python list tech:
to iterate all the elements in a list:
     for idx in range(0,len(list)):
          
bit manipulation tech:
    def getbit(num):
        res = []
        while(num>0):
            tmp = num%2
            res.append(tmp)
            num = int((num-tmp)/2)
    
“”“



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res= [[]] # just include special case []
        
        length_of_nums = len(nums) 
        for num in range(1,2**length_of_nums):   # brute force all the possiblity
            
            count_arr= []
             
            while(num>0):
                t= num%2
                count_arr.append(t)
                num = int((num-t)/2)
            
            tmp_list=[]
            for h in range(0,length_of_nums):  # for each count number we get a distinct array represent the situation
                 # from the situation, we get a tmp list which is a subset
                if(h<len(count_arr) and count_arr[h]==1):           
                    tmp_list.append(nums[h])
                                    
            res.append(tmp_list)
        
        return res
