class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_itr = 0 

        if len(s) <= 0:
            return True


        for x in range(len(t)):

            l1 = s[s_itr]
            l2 = t[x]

            if l1 == l2:
                s_itr += 1
            
            if s_itr == len(s):
                return True
            
        
        return False
        


