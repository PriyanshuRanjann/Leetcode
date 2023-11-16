class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer=0
        t_pointer=0
        while s_pointer<len(s) and t_pointer<len(t):
            if s[s_pointer]==t[t_pointer]:
                s_pointer+=1
            t_pointer+=1
        return s_pointer==len(s)
        '''
        new=""
        for i in t:
            if i in s:
                new+=i
        if new==s:
            return True
        else:
            return False
        '''