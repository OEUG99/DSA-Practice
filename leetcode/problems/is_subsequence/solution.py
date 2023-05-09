class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ptr = 0
        t_ptr = 0

        if len(s) < 1:
            return True

        for t_ptr, t_val in enumerate(t):
            
            if s_ptr +1 > len(s) or t_ptr +1 > len(t):
                break

            # if match we move to the next
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1
                continue

        return s_ptr == len(s)

            


            

        
        