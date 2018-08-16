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
       
