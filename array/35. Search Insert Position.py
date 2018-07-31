        
        
        
        
        
 # ref leetcode
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
        return len(nums)
        
 # my sol 
     def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        if nums[0] > target :
            return 0
        if nums[-1] < target:
            return len(nums)
        
        for i in range(0,len(nums)): # len(nums) >=1  i from 0 to len(nums)-1
            if nums[i] == target:
                return i
            elif nums[i+1] > target and nums[i] < target :
                return i+1
