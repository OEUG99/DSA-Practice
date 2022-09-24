class Solution {
    public void rotate(int[] nums, int k) {
        int maxLength = nums.length -1;
        k--;
        
        if (maxLength == 0){
            return;
        }
        
        k = k % (nums.length); // if k is greater than maxLegnth we can reduce to via modulus and get same result but not have to worry about out of bounds.
        
        
        nums = reverse(nums, 0, maxLength); // reversing whole array
        nums = reverse(nums, 0, k); // reversing k sub-array
        nums = reverse(nums, k+1, maxLength); // reversing leftover sub array;
        
        
    }
    
    public int[] reverse(int[] nums, int start, int end){
        int temp = 0;
        while (start < end){
            temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
            start++;
            end--;
        }
        return nums;
    }
        
        
        
}