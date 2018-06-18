def getbit(num):
        """
        :type num: int
        :rtype: List
        """
        ret_list=[]
        while(num>0):
            t= num%2
            ret_list.append(t)
            num = int((num-t)/2)
        return ret_list
            
