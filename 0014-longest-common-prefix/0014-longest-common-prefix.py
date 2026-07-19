class Solution(object):
    def longestCommonPrefix(self, strs):
        ret = ''
        if (1 <= len(strs) <= 200):
            minn = 200
            for i in range(len(strs)):
                if 1<= len(strs[i]) <= 200:
                    if (len(strs[i])< minn):
                        minn = len(strs[i])
                else:
                    return ret
            i,j= 0,0
            while(i<=minn-1):
                for k in range(len(strs)):
                    flag = True
                    cmmn = strs[0][j]
                    if cmmn != strs[k][j]:
                        flag = False
                        break
                if flag:
                    ret += cmmn
                    j += 1
                else:
                    return ret
                i += 1
            return ret

        
