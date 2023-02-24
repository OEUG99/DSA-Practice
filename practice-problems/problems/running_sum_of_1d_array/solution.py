class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for x in range(len(nums)):
            result.append(sum(nums[:x+1]))
        
        return result
        
