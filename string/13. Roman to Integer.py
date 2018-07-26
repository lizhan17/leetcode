class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict={}
        
        dict["I"]=1
        dict["V"]=5
        dict["X"]=10
        dict["L"]=50
        dict["C"]=100
        dict["D"]=500
        dict["M"]=1000
        
        res = 0
        
        length = len(s)
        for i in range(0,length):
            if i== length-1 or dict[s[i]] >= dict[s[i+1]]:
                res = res + dict[s[i]]
            else:
                res = res - dict[s[i]]
        
        return res
