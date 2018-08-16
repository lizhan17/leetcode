class Solution:
’‘’
要知道数据结构是固定的
那么你的思路还是固定的
比如数列
你也就能从左到右

快一点的（涉及到排序的）可能有从又到左

问题不是用人的方法
要从电脑的角度看


还有一种思路是从例子来
毕竟现实里 还是从例子开始做问题
‘’‘
    # @return an integer
   # ref https://blog.csdn.net/wangyaninglm/article/details/51068831
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0 # 局部 要改变的
        usedChar ={} # 全局变量
        
        for i in range(len(s)):  #从左开始一个个看
            if s[i] in usedChar and start <= usedChar[s[i]]: #如果这个在 字母在里面并且在 包围圈里 那么
                start = usedChar[s[i]]+1 
            else: # 否则比较长度（以这个为截止）
                maxLength = max(maxLength,i-start+1)
            usedChar[s[i]]= i
        return maxLength
       

 
# my sol beat 83%
        
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        从算法角度 这个题目可解决
        因为 你可以bf 一个个看
        
        
        
        '''
        strLength = len(s)
        # any must has a achor
        
        if strLength == 0:
            return ''
        if strLength == 1:
            return s[0]
        if strLength == 2 and s[0]==s[1]:
            return s
        elif strLength == 2 and s[0]!=s[1]:
            return s[0]
            
        
        # case length >3
        
        maxLength = 1
        length = 0
        res = s[0]
        
     
        for i in range(0,strLength-1):  #!!!   0<i<lenth
            if 2*(strLength-i) > maxLength:        # weak may have extra execute
                if s[i]==s[i+1]:
                    l = i
                    r = i+1
                    while( l>-1 and r< strLength and s[l]==s[r]):
                        l = l-1
                        r = r+1
                # step back; we may have l==0 -> l=-1 -> l=0
                    l=l+1
                    r=r-1
                
                    length = r-l+1 # this time s[l]==s[r]
                    
                    if length > maxLength:
                        maxLength = length #update length
                        res = s[l:r+1] # update result
                if i+2< strLength and s[i] ==s[i+2]:
                    l = i  
                    r = i + 2
                    while(l>-1 and r<strLength and s[l] == s[r] ):
                        l = l-1
                        r = r+1
                    l=l+1
                    r=r-1    
                    length = r-l+1
                
                    if length > maxLength:
                        maxLength = length #update length
                        res = s[l:r+1] # update result
            else:
                return res
        return res
