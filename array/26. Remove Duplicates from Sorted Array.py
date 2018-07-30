class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<2):
            return len(nums)
        
        if (len(nums) ==2):
            if nums[0]==nums[1]:
                return 1
            else:
                return 2
            
        for i in range(0,len(nums)-1): # (len 0 , 1, 2,)
            if nums[i]==nums[i+1]:
                for j in range(i,len(nums)-1):
                    nums[j]=nums[j+1]
                    nums.pop()
        
        return len(nums)
        
     # true solution is by 公瑾tm
     
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 
        slow = fast = 0
        while fast <= len(nums) - 1:
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1
            fast += 1
        return slow + 1
