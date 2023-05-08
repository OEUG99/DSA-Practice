class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Sliding Window - We will leave a 1 element gap between left amd right amd slide it to find solution.
        left = 0
        for right, val in enumerate(nums):    
            
            left_pos = nums[:left]
            right_pos = nums[right+1:]
            value = left
            
            if (sum(left_pos) == sum(right_pos)):
                return value
            
            left +=1

        return -1