class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        leftSum = 0
        rightSum = sum(nums)

        """
        rightSum starts as the entire array,
        leftSum is an empty array.

        step 1:
        create a first pivot at itr by removing it from 
        rightSum

        step 2:
        Now both arrays don't have that value, so we check if
        this removed value is the right pivot.

        step 3:
        if not right pivot, we add the previous pivot to the left sub array. 

        step 4:
        repeat
        """

        for itr, num in enumerate(nums):
            rightSum -= num

            if (leftSum == rightSum):
                return itr
    
            leftSum += num
            

        return -1 




            


