class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        map_s_t = {}
        map_t_s = {}

        for x, val in enumerate(s):
            l1 = s[x]
            l2 = t[x]

            # If l1 exist in the mapping
            if l1 in map_s_t:
                # if it exists but is not 1 to 1 return false
                if map_s_t[l1] != l2:
                    return False
            
            # if l1 not in the mapping:
            else: 
                # checking if the mapping the other way.
                if l2 in map_t_s:
                    return False

            # mapping both characters if all checks pass:
            map_s_t[l1] = l2
            map_t_s[l2] = l1

        return True




