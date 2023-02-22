class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for x, num in enumerate(nums):

            if x+1 > len(nums):
                break

            result.append(sum(nums[:x+1]))

        return result
