class Solution:
    def intToRoman(self, num: int) -> str:
        d={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        ret=''
        for i in d.keys():
            if num//i>=1:
                c=num//i
                ret+=(d[i]*c)
                num=num%i
        return ret