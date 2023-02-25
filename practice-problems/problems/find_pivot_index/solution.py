class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = sum(nums)


        for x, y in enumerate(nums):

            right -= y

            if left == right:
                return x
            
            left += y
        
        return -1
            
            







            


