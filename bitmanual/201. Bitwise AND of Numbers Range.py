"""
date:2018/06/20

bit operation in python:

Binary AND:
(a & b) (means 0000 1100)
Binary OR:
(a | b) = 61 (means 0011 1101)

^ Binary XOR:
It copies the bit if it is set in one operand but not both.
(a ^ b) = 49 (means 0011 0001)


<< Binary leftshift:


>> Binary rightshift:

why we use in this problem:
to get the ith bit of 


python teck: step back 
for i in range(32)[::-1]:

x = x | y  
equals 
x|=y



m>>i&1

just get the ith bit 


|= 1 << i

add the ith bit to a 000000010000 number
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        ret = 0
        for i in range(32)[::-1]:  # 31,30,29....0
             # we compare from the highest bit 31th bit(32)
            if m>>i != n>>i:  # if m's i bit not same with n's i bit
              
                break    # break  why: because they are not same otherwise keep m's i bit
            ret |= (m>>i&1)<<i 
            # give ret the bit of m
        return ret
#  200ms

#ref https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56780/Short-1-liners-in-Python-with-explanation




if m == 0:
            return 0
        res = 1
        while m != n:
            m >>= 1
            n >>= 1
            res <<= 1
        return m * res
#ref: leetcode just 100ms
