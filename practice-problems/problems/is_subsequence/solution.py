class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sptr, tptr = 0, 0

        if len(s) <= 0:
            return True

        while(sptr < len(s) and tptr < len(t)):
            if s[sptr] == t[tptr]:
                sptr += 1
            
            tptr +=1

            if sptr == len(s):
                return True

        return False 
        




                

