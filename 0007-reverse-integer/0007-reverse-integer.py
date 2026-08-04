class Solution(object):
    def reverse(self, x):
        
        t=int(str(abs(x))[::-1])
        if -2**31 > t or t>(2**31-1):
            return 0
        return t if x>0 else -t     
        