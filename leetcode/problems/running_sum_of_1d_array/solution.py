class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []

        for x,y in enumerate(nums):
            output.insert(x,sum(nums[:x+1]))

        return output
                


