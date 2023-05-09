class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        map_s_t = {}
        map_t_s = {}

        result = True

        for x,char in enumerate(s):

            l1 = char
            l2 = t[x]

            # if letter from first word in map already, and that mapping does not equal the new second letter
            if (l1 in map_s_t.keys() and map_s_t[l1] != l2) or (l2 in map_t_s.keys() and map_t_s[l2] != l1):
                result = False
                break
            
            if l1 not in map_s_t.keys() and l1 not in map_s_t.values() and l2 not in map_t_s.keys() and l2 not in map_t_s.values():
                map_s_t[l1] = l2
                map_t_s[l2] = l1
                continue


        return result


            

           

            

            