class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for y, _ in enumerate(nums):
            
            if y >= len(nums):
                break

            result.append(self.sum(y+1, nums))

        return result

    def sum(self, count, nums):
        sum = 0
        for x in range(count):
            sum = sum + nums[x]

        return sum
        
    