class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        rightSum = sum(nums)

        for x in range(len(nums)):
            
            rightSum -= nums[x]


            if rightSum == leftSum:
                return x

            leftSum += nums[x]
        
        return -1


            
            







            


