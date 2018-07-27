class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # brute force 
        # outer loop : start of the substring 
        
        # inner loop: the end of the substring 
        # to get the no repeat element 
        # we need to no not in s[]
        
        if len(s)<=1:
            return len(s)
        
        # len(s)>=2
        start = 0
        max_length = 1
        
        while(start < len(s)-1):
            tmp_str = s[start] # !important from the start
            tmp_length = 1
            for next_char in range(start+1,len(s)):
                if s[next_char] not in tmp_str:
                    tmp_str = tmp_str+ s[next_char]
                    tmp_length = tmp_length+1
                else:
                    # this is the longest substring we can found if we start at s[start]
                    break
            # lets update the max_length 
            if tmp_length > max_length :
                max_length = tmp_length
            start = start +1 
        # we can op in this while loop(no need to until last element)
        return max_length
    
