class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map_s_t = {}
        map_t_s = {}

        for x, val, in enumerate(s):
            l1 = s[x]
            l2 = t[x]

            # checking if l1 is mapped, if it we skip to next char if it's value is mapped to l2
            if l1 in map_s_t:
                if map_s_t.get(l1) == l2:
                    continue
                else:
                    return False

            # if not in map
            else:
                # we check if it's in l2 map and mapped to a different character, if already mapped return False as it wont be 1 to 1 and Isomorphic
                if l2 in map_t_s.keys():
                    return False

            # If neither are mapped, we we shall map both together.
            map_s_t[l1] = l2
            map_t_s[l2] = l1

        return True
            

